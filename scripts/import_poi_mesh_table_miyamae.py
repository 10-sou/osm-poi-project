import json
import pandas as pd
from sqlalchemy import create_engine

# JSONファイルパス
json_path = "/home/t012/osm-poi-project/output/poi_mesh_table_hospitals_convenience_miyamae.json"

# カラム名の変換マッピング（日本語 → 英語）
rename_map = {
    "セブン-イレブン": "seven_eleven",
    "ファミリーマート": "family_mart",
    "ローソン": "lawson",
    "かねこクリニック": "kaneko_clinic",
    "一般財団法人　聖マリアンナ会　東横恵愛病院": "higashiyoko_hospital",
    "医療法人愛生会有馬病院": "arima_hospital",
    "医療法人花咲会　かわさき記念病院": "kawasaki_memorial",
    "愛生会有馬病院": "arima_hospital_alt",
    "聖マリアンナ会東横恵愛病院": "higashiyoko_hospital_alt",
    "聖マリアンナ医科大学病院": "marianna_university_hospital"
}

# JSON読み込み
with open(json_path, encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# カラム名を英語に変換（MySQL用）
df.rename(columns=rename_map, inplace=True)

# 不要な日本語カラムの削除
drop_cols = set(df.columns) - set(rename_map.values()) - {"mesh_id"}
if drop_cols:
    df.drop(columns=drop_cols, inplace=True)

# MySQLに接続（必要に応じてパスワードやDB名変更）
engine = create_engine("mysql+pymysql://laravel_user:0306souta@localhost/laravel_app")

# データベースへ登録
df.to_sql("mesh_tags_miyamae", con=engine, if_exists="append", index=False)

print("✅ mesh_tags_miyamae テーブルへの登録が完了しました")
