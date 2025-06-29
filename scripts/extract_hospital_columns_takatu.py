import json

# 入力ファイルパス
input_path = "/home/t012/osm-poi-project/output/tmp-filtered.geojson"

# 出力ファイルパス
output_path = "/home/t012/osm-poi-project/output/hospital_columns_takatu.json"

# GeoJSONを読み込む
with open(input_path, encoding="utf-8") as f:
    data = json.load(f)

# 病院名の抽出
hospital_names = set()
for feature in data["features"]:
    props = feature.get("properties", {})
    if props.get("amenity") in ["hospital", "clinic"]:
        name = props.get("name") or props.get("name:ja") or props.get("official_name") or "Unknown"
        hospital_names.add(name)

# ソートしてリスト化
hospital_names_list = sorted(hospital_names)

# JSON形式で出力
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(hospital_names_list, f, ensure_ascii=False, indent=2)

print(f"病院名リストを {output_path} に出力しました。")
