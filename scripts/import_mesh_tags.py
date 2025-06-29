import json
import pandas as pd
from sqlalchemy import create_engine

# JSONファイルのパス
json_path = "/home/t012/osm-poi-project/output/poi_mesh_table.json"

# カラム名の変換マッピング（日本語 → 英語）
rename_map = {
    "セブン-イレブン": "seven_eleven",
    "ファミリーマート": "family_mart",
    "ローソン": "lawson",
    "ハートフル川崎病院": "heartful_hospital",
    "総合高津中央病院": "takatsu_hospital"
}

# JSONを読み込んでDataFrameに変換
with open(json_path, encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# カラム名を英語に変換（MySQLテーブルに合わせる）
df.rename(columns=rename_map, inplace=True)

# 不要な日本語カラムが残っていないか確認して削除
drop_cols = set(df.columns) - set(rename_map.values()) - {"mesh_id"}
if drop_cols:
    df.drop(columns=drop_cols, inplace=True)

# MySQL接続（パスワードは環境に応じて変更）
engine = create_engine("mysql+pymysql://laravel_user:0306souta@localhost/laravel_app")

# データベースに挿入（append: 追記、index: Falseでid列は無視）
df.to_sql("mesh_tags", con=engine, if_exists="append", index=False)

print("✅ データ登録完了")
