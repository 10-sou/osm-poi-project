import json
from shapely.geometry import shape
from collections import defaultdict

# === ファイル読み込み ===
with open("/home/t012/osm-poi-project/output/kawasaki_高津区_mesh.geojson", encoding="utf-8") as f:
    mesh_data = json.load(f)

with open("/home/t012/osm-poi-project/output/tmp-filtered.geojson", encoding="utf-8") as f:
    poi_data = json.load(f)

# === POIデータの整形（重心＋名前抽出）===
poi_entries = []
for feature in poi_data["features"]:
    centroid = shape(feature["geometry"]).centroid
    props = feature["properties"]
    name = props.get("name") or props.get("name:ja") or props.get("brand") or "Unknown"
    amenity = props.get("amenity")

    # コンビニまたはクリニック（amenity = clinic）のみ抽出
    if (
        name in {"セブン-イレブン", "ファミリーマート", "ローソン"}
        or  amenity in {"clinic", "hospital"}
    ):
        poi_entries.append({
            "name": name,
            "geometry": centroid,
            "original_properties": props,
            "original_geometry": feature["geometry"]
        })

# === メッシュリスト構築 ===
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

# === POIとメッシュの対応付け ===
matched_pois = []
brand_to_found_mesh_ids = defaultdict(set)

for poi in poi_entries:
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
            break

# === 欠損メッシュIDの算出 ===
missing_meshes = {}
for brand, found_mesh_ids in brand_to_found_mesh_ids.items():
    missing = sorted(all_mesh_ids - found_mesh_ids)
    if missing:
        missing_meshes[brand] = missing

# === ファイル出力 ===
output_dir = "/home/t012/osm-poi-project/output"

with open(f"{output_dir}/poi_with_mesh_takatu.geojson", "w", encoding="utf-8") as f:
    json.dump({
        "type": "FeatureCollection",
        "features": matched_pois
    }, f, ensure_ascii=False, indent=2)

with open(f"{output_dir}/missing_meshes_takatu.json", "w", encoding="utf-8") as f:
    json.dump({"missing_meshes_takatu": missing_meshes}, f, ensure_ascii=False, indent=2)

print("✅ 出力完了:")
print(f"  - {output_dir}/poi_with_mesh_takatu.geojson")
print(f"  - {output_dir}/missing_meshes_takatu.json")
