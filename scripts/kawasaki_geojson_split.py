import geopandas as gpd

# 入力ファイル（川崎市全体）
input_path = "/home/t012/osm-poi-project/output/kawasaki_city.geojson"

# 出力ディレクトリ
output_dir = "/home/t012/osm-poi-project/output"

# 読み込み
gdf = gpd.read_file(input_path)

# 分割対象の区名リスト
target_wards = ["宮前区", "高津区", "麻生区"]

# 各区ごとに抽出・保存
for ward in target_wards:
    ward_gdf = gdf[gdf["N03_005"] == ward]
    output_path = f"{output_dir}/kawasaki_{ward}.geojson"
    ward_gdf.to_file(output_path, driver="GeoJSON")
    print(f"✅ {ward} を保存しました → {output_path}")
