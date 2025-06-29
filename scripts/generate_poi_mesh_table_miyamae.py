import json
import pandas as pd
from shapely.geometry import shape

# === 入力ファイルパス ===
poi_geojson_path = "/home/t012/osm-poi-project/output/poi_with_mesh.geojson"
missing_json_path = "/home/t012/osm-poi-project/output/missing_meshes_miyamae.json"
hospital_col_path = "/home/t012/osm-poi-project/output/hospital_columns_miyamae.json"

# === 出力ファイルパス ===
output_path = "/home/t012/osm-poi-project/output/poi_mesh_table_with_coords_miyamae.json"

# === ファイル読み込み ===
with open(poi_geojson_path, encoding="utf-8") as f:
    poi_data = json.load(f)

with open(missing_json_path, encoding="utf-8") as f:
    missing_data = json.load(f)

with open(hospital_col_path, encoding="utf-8") as f:
    hospital_cols_data = json.load(f)
hospital_names = hospital_cols_data.get("hospital_columns", [])

# === コンビニ名（手動定義）===
convenience_names = ["セブン-イレブン", "ファミリーマート", "ローソン"]

# === 対象の全タグ ===
target_tags = set(hospital_names + convenience_names)

# === POIのタグごとの存在メッシュと座標を抽出 ===
existing_map = {}
mesh_tag_coords_map = {}  # mesh_id -> { tag -> [lon, lat] }

for feature in poi_data["features"]:
    props = feature["properties"]
    geometry = feature.get("geometry")
    tag = props.get("name") or props.get("brand") or "Unknown"
    mesh_id = props.get("mesh_id")

    if tag in target_tags and mesh_id is not None:
        existing_map.setdefault(tag, set()).add(mesh_id)

        if geometry:
            try:
                geom = shape(geometry)
                centroid = geom.centroid
                lon, lat = centroid.x, centroid.y
                mesh_tag_coords_map.setdefault(mesh_id, {})
                if tag not in mesh_tag_coords_map[mesh_id]:
                    mesh_tag_coords_map[mesh_id][tag] = [lon, lat]
            except Exception as e:
                print(f"⚠️ ジオメトリ処理エラー（tag: {tag}）: {e}")

# === 縦長形式データに変換 ===
records = []
all_tags = set(existing_map) | set(missing_data.get("missing_meshes_miyamae", {}).keys())
for tag in all_tags:
    if tag not in target_tags:
        continue
    exists_set = existing_map.get(tag, set())
    missing_set = set(missing_data["missing_meshes_miyamae"].get(tag, []))

    for mesh_id in exists_set:
        records.append({"tag": tag, "mesh_id": mesh_id, "status": "exists"})

    for mesh_id in missing_set:
        if mesh_id not in exists_set:
            records.append({"tag": tag, "mesh_id": mesh_id, "status": "missing"})

# === ワイド形式に変換 ===
df = pd.DataFrame(records)
df["value"] = df["status"].map({"exists": 1, "missing": 0})
wide_df = df.pivot_table(index="mesh_id", columns="tag", values="value", fill_value=0).reset_index()

# === POIごとの座標を追加 ===
wide_df["poi_coords"] = wide_df["mesh_id"].map(lambda mesh_id: mesh_tag_coords_map.get(mesh_id, {}))

# === 列順序の整理 ===
columns = ["mesh_id"] + sorted(wide_df.columns.drop(["mesh_id", "poi_coords"]).tolist()) + ["poi_coords"]
wide_df = wide_df[columns]

# === JSON出力 ===
wide_df.to_json(output_path, orient="records", force_ascii=False, indent=2)

print(f"✅ 宮前区：POI座標付きJSONを出力しました → {output_path}")
