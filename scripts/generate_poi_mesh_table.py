import json
import pandas as pd

# === ファイル読み込み ===
with open("/home/t012/osm-poi-project/output/poi_with_mesh.geojson", encoding="utf-8") as f:
    poi_data = json.load(f)

with open("/home/t012/osm-poi-project/output/missing_meshes.json", encoding="utf-8") as f:
    missing_data = json.load(f)

# === POIのタグごとの存在メッシュを抽出 ===
existing_map = {}  # tag -> set of mesh ids
for feature in poi_data["features"]:
    props = feature["properties"]
    tag = props.get("name") or props.get("brand") or "Unknown"
    mesh_id = props.get("mesh_id")
    if tag and mesh_id is not None:
        existing_map.setdefault(tag, set()).add(mesh_id)

# === 縦長データフレームの作成 ===
records = []
all_tags = set(existing_map) | set(missing_data["missing_meshes"])
for tag in all_tags:
    exists_set = existing_map.get(tag, set())
    missing_set = set(missing_data["missing_meshes"].get(tag, []))

    # 存在するメッシュ
    for mesh_id in exists_set:
        records.append({"tag": tag, "mesh_id": mesh_id, "status": "exists"})
    
    # 存在しないメッシュ（重複除外）
    for mesh_id in missing_set:
        if mesh_id not in exists_set:
            records.append({"tag": tag, "mesh_id": mesh_id, "status": "missing"})

df = pd.DataFrame(records)

# === ワイドフォーマットへ変換（中間テーブル）===
df["value"] = df["status"].map({"exists": 1, "missing": 0})
wide_df = df.pivot_table(index="mesh_id", columns="tag", values="value", fill_value=0).reset_index()

# 列順序の整え（mesh_id + タグ名順）
wide_df = wide_df[["mesh_id"] + sorted(wide_df.columns.drop("mesh_id"))]



# === JSON出力 ===
output_json_path = "/home/t012/osm-poi-project/output/poi_mesh_table.json"
wide_df.to_json(output_json_path, orient="records", force_ascii=False, indent=2)
print(f"✅ JSONファイルを出力しました: {output_json_path}")
