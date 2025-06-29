import json
import pandas as pd
from shapely.geometry import shape

# === 入力ファイルパス ===
poi_path = "/home/t012/osm-poi-project/output/poi_with_mesh_takatu.geojson"
missing_path = "/home/t012/osm-poi-project/output/missing_meshes_takatu.json"

# === 出力ファイルパス ===
output_json_path = "/home/t012/osm-poi-project/output/poi_mesh_table_with_coords_takatu.json"

# === ファイル読み込み ===
with open(poi_path, encoding="utf-8") as f:
    poi_data = json.load(f)

with open(missing_path, encoding="utf-8") as f:
    missing_data = json.load(f)["missing_meshes_takatu"]

# === POIのタグごとの存在メッシュと座標を抽出 ===
existing_map = {}
mesh_tag_coords_map = {}  # mesh_id -> { tag -> [lon, lat] }

for feature in poi_data["features"]:
    props = feature.get("properties", {})
    geometry = feature.get("geometry")
    tag = props.get("name") or props.get("brand") or "Unknown"
    mesh_id = props.get("mesh_id")

    if tag and mesh_id is not None:
        existing_map.setdefault(tag, set()).add(mesh_id)

        # すべてのジオメトリタイプに対応（重心使用）
        if geometry:
            try:
                centroid = shape(geometry).centroid
                lon, lat = centroid.x, centroid.y
                mesh_tag_coords_map.setdefault(mesh_id, {})
                if tag not in mesh_tag_coords_map[mesh_id]:
                    mesh_tag_coords_map[mesh_id][tag] = [lon, lat]
            except Exception as e:
                print(f"⚠️ ジオメトリ処理失敗: {e}")

# === タグごとに存在・欠損メッシュのレコード作成 ===
records = []
all_tags = set(existing_map) | set(missing_data)
for tag in all_tags:
    exists_set = existing_map.get(tag, set())
    missing_set = set(missing_data.get(tag, []))

    for mesh_id in exists_set:
        records.append({"tag": tag, "mesh_id": mesh_id, "status": "exists"})

    for mesh_id in missing_set:
        if mesh_id not in exists_set:
            records.append({"tag": tag, "mesh_id": mesh_id, "status": "missing"})

df = pd.DataFrame(records)

# === ワイド形式に変換（中間テーブル）===
df["value"] = df["status"].map({"exists": 1, "missing": 0})
wide_df = df.pivot_table(index="mesh_id", columns="tag", values="value", fill_value=0).reset_index()

# === POIごとの座標（辞書形式）を追加 ===
wide_df["poi_coords"] = wide_df["mesh_id"].map(lambda mesh_id: mesh_tag_coords_map.get(mesh_id, {}))

# === 列順整理 ===
columns = ["mesh_id"] + sorted(wide_df.columns.drop(["mesh_id", "poi_coords"]).tolist()) + ["poi_coords"]
wide_df = wide_df[columns]

# === JSON出力 ===
wide_df.to_json(output_json_path, orient="records", force_ascii=False, indent=2)

print(f"✅ 高津区：POI座標付きJSONを出力しました → {output_json_path}")
