import json
import pandas as pd

# 入力ファイルと出力ファイルのパス
input_path = "/home/t012/osm-poi-project/output/poi_mesh_table_miyamae.json"
output_path = "/home/t012/osm-poi-project/output/hospital_columns_miyamae.json"

# JSON読み込み
with open(input_path, encoding="utf-8") as f:
    data = json.load(f)

# DataFrameに変換
df = pd.DataFrame(data)

# 「病院」または「クリニック」を含むカラム名を抽出
hospital_columns = [col for col in df.columns if "病院" in col or "クリニック" in col]

# 出力ファイルに保存（JSON形式）
with open(output_path, "w", encoding="utf-8") as f:
    json.dump({"hospital_columns": hospital_columns}, f, ensure_ascii=False, indent=2)

print(f"✅ 病院・クリニックのカラム名を出力しました: {output_path}")
