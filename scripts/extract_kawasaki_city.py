import geopandas as gpd

# シェープファイルの絶対パス
shapefile_path = "/home/t012/osm-poi-project/input/extracted_gml/N03-20240101_14.shp"

# 読み込み
gdf = gpd.read_file(shapefile_path)

# 川崎市に該当するレコードを抽出
kawasaki_gdf = gdf[gdf["N03_004"].str.contains("川崎市", na=False)]

# ✅ 出力パスをプロジェクトの output ディレクトリに変更
output_path = "/home/t012/osm-poi-project/output/kawasaki_city.geojson"

# GeoJSONとして保存
kawasaki_gdf.to_file(output_path, driver="GeoJSON")

print("✅ GeoJSONを書き出しました:", output_path)




"""
#列名出力
print(gdf.columns)

#表形式にして列の中身などをざっくり見る
#print(gdf[['N03_001', 'N03_002', 'N03_003', 'N03_004', 'N03_005', 'N03_007']].head(10))

#区名一覧
print(gdf["N03_005"])

#市名一覧
print(gdf["N03_004"])

#市で絞って区名を一覧にする
print(gdf[gdf["N03_004"] == "川崎市"]["N03_005"])
"""




"""
kawasaki_gdf = gdf[gdf["N03_004"].str.contains("川崎市", na=False)]
print(kawasaki_gdf[["N03_001", "N03_003", "N03_004"]].head())
print(kawasaki_gdf["N03_004"].drop_duplicates().tolist())
"""


"""
# ✅ 成功したかどうか簡易チェック
print(gdf.columns)
print("✅ 行数:", len(gdf))
print("✅ 列名:", gdf.columns.tolist())
print("✅ 最初の1行:\n", gdf.head(1))
"""

"""
# 読み込み（shapely 1.8系であれば直接読み込み可能）
gdf = gpd.read_file(shapefile_path)

# 必要な列だけ取り出して重複除去
df_codes = gdf[["N03_004", "N03_007"]].dropna().drop_duplicates()

# ソートして表示
df_codes_sorted = df_codes.sort_values("N03_004")

print("🏷️ 市区町村と対応コード:")
for _, row in df_codes_sorted.iterrows():
    print(f"- {row['N03_004']}: {row['N03_007']}")
"""

"""
# 重複を除いた行政区名一覧を表示
admin_names = gdf["N03_004"].dropna().unique()

print("📍 行政区名一覧:")
for name in sorted(admin_names):
    print("-", name)
"""

"""
# 川崎市に該当する地物だけ抽出
kawasaki_gdf = gdf[gdf["N03_004"].str.contains("川崎市", na=False)]

# 出力先
output_path = "/home/t012/osm-poi-project/input/kawasaki_city.geojson"
kawasaki_gdf.to_file(output_path, driver="GeoJSON")

print("✅ GeoJSONを書き出しました:", output_path)
"""
