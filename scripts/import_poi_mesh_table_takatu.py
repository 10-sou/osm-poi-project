import json
import pandas as pd
from sqlalchemy import create_engine

# === 入力JSONファイルパス ===
json_path = "/home/t012/osm-poi-project/output/poi_mesh_table_takatu.json"

# === カラム名の変換マッピング（日本語 → 英語）===
rename_map = {
    "セブン-イレブン": "seven_eleven",
    "ファミリーマート": "family_mart",
    "ローソン": "lawson",
    "ハートフル川崎病院": "heartful_hospital",
    "総合高津中央病院": "takatsu_hospital"
}

# === JSON読み込み ===
with open(json_path, encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# === カラム名を英語に変換（MySQL用）===
df.rename(columns=rename_map, inplace=True)

# === 不要な日本語カラムの削除 ===
drop_cols = set(df.columns) - set(rename_map.values()) - {"mesh_id"}
if drop_cols:
    df.drop(columns=drop_cols, inplace=True)

# === MySQL接続設定（パスワードやDB名は適宜調整）===
engine = create_engine("mysql+pymysql://laravel_user:0306souta@localhost/laravel_app")

# === MySQLへ保存（テーブル名: mesh_tags_takatu）===
df.to_sql("mesh_tags_takatu", con=engine, if_exists="append", index=False)

print("✅ mesh_tags_takatu テーブルへの登録が完了しました")
