import json
from shapely.geometry import shape
from collections import defaultdict

# === Step 1: GeoJSONファイル読み込み ===
with open("/home/t012/osm-poi-project/output/kawasaki_高津区_mesh.geojson", encoding="utf-8") as f:
    mesh_data = json.load(f)

with open("/home/t012/osm-poi-project/output/tmp-poi-buildings.geojson", encoding="utf-8") as f:
    poi_data = json.load(f)

# === Step 2: POIを重心・名前とともにリスト化 ===

poi_entries = []
for feature in poi_data["features"]:
    centroid = shape(feature["geometry"]).centroid
    #辞書名[]でアクセス
    props = feature["properties"]
    #getで辞書型の要素にアクセス
    name = props.get("name") or props.get("name:ja") or props.get("brand") or "Unknown"
    poi_entries.append({
        "name": name,
        "geometry": centroid,
        "original_properties": props,
        "original_geometry": feature["geometry"]
    })
        """
        {
  "name": "セブン-イレブン",
  "geometry": <shapely.geometry.Point object at 0x12345678>,  # centroid座標
  "original_properties": {
    "name": "セブン-イレブン",
    "brand": "7-ELEVEN",
    "building": "yes",
    ...
  },
  "original_geometry": {
    "type": "LineString",
    "coordinates": [
      [139.6285686, 35.574712],
      [139.6286647, 35.5745411],
      ...
    ]
  }
}
"""
# === Step 3: メッシュを index 順で格納 ===
mesh_list = []
all_mesh_ids = set()
for i, feature in enumerate(mesh_data["features"]):
    polygon = shape(feature["geometry"])
    properties = feature.get("properties", {})
    mesh_list.append({
        "geometry": polygon,
        "properties": properties,
        "index": i
    })
    all_mesh_ids.add(i)
    """
    {
    "geometry": <Shapely Polygon オブジェクト>,
    "properties": {
        "N03_001": "神奈川県",
        "N03_004": "川崎市",
        "N03_005": "高津区",
        "mesh_id": <もともとの属性値>,
    },
    "index": 0  # ファイル順の連番として付けたmesh_id（POI割り当てで使う）
}
"""

# === Step 4: POIとメッシュの対応判定 ===
matched_pois = []
brand_to_found_mesh_ids = defaultdict(set)

for poi in poi_entries:
    matched = False
    for mesh in mesh_list:
        if mesh["geometry"].contains(poi["geometry"]):
            props_with_mesh = poi["original_properties"].copy()
            props_with_mesh["mesh_id"] = mesh["index"]
            matched_pois.append({
                "type": "Feature",
                "geometry": poi["original_geometry"],
                "properties": props_with_mesh
            })
            brand_to_found_mesh_ids[poi["name"]].add(mesh["index"])
            matched = True
            break

# === Step 5: ブランドごとのmissingメッシュIDを求める ===
missing_meshes = {}
for brand, found_mesh_ids in brand_to_found_mesh_ids.items():
    missing = sorted(all_mesh_ids - found_mesh_ids)
    if missing:
        missing_meshes[brand] = missing

# === Step 6: 結果をファイル出力 ===
output_dir = "/home/t012/osm-poi-project/output"

# ① POI + メッシュ情報（GeoJSON形式）
poi_geojson = {
    "type": "FeatureCollection",
    "features": matched_pois
}
with open(f"{output_dir}/poi_with_mesh.geojson", "w", encoding="utf-8") as f:
    json.dump(poi_geojson, f, ensure_ascii=False, indent=2)

# ② ブランドごとの欠損メッシュ（JSON形式）
with open(f"{output_dir}/missing_meshes.json", "w", encoding="utf-8") as f:
    json.dump({"missing_meshes": missing_meshes}, f, ensure_ascii=False, indent=2)

print("✅ 出力完了:")
print(f"  - {output_dir}/poi_with_mesh.geojson")
print(f"  - {output_dir}/missing_meshes.json")
