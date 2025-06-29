import geopandas as gpd
from shapely.geometry import box
import os

# メッシュサイズ（500m ≒ 0.005度程度）
mesh_size_deg = 0.005

# 対象区とファイルパス
wards = ["高津区", "麻生区", "宮前区"]
input_dir = "/home/t012/osm-poi-project/output"
output_dir = "/home/t012/osm-poi-project/output"

for ward in wards:
    input_path = f"{input_dir}/kawasaki_{ward}.geojson"
    gdf = gpd.read_file(input_path)

    # 外接バウンディングボックス取得
    minx, miny, maxx, maxy = gdf.total_bounds

    # メッシュのポリゴンを生成
    mesh_polygons = []
    x = minx
    while x < maxx:
        y = miny
        while y < maxy:
            cell = box(x, y, x + mesh_size_deg, y + mesh_size_deg)
            mesh_polygons.append(cell)
            y += mesh_size_deg
        x += mesh_size_deg

    # メッシュ GeoDataFrame 作成
    mesh_gdf = gpd.GeoDataFrame(geometry=mesh_polygons, crs=gdf.crs)

    # 区の境界で内部メッシュを抽出
    clipped = gpd.overlay(mesh_gdf, gdf, how="intersection")

    # ✅ geometryはそのままで、連番の mesh_id を追加
    clipped = clipped.reset_index(drop=True)
    clipped["mesh_id"] = clipped.index + 1  # 1からスタート

    # 出力ファイルパス
    output_path = f"{output_dir}/kawasaki_{ward}_mesh.geojson"
    clipped.to_file(output_path, driver="GeoJSON")

    print(f"✅ {ward} のメッシュを保存しました → {output_path}")
