<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;

class MeshTagController extends Controller
{
   public function tagOptions(Request $request)
{
    $ward = $request->query('ward');
    $category = $request->query('category');

    // 対象モデルを選択
    if ($ward === 'takatu') {
        $modelClass = \App\Models\TakatuMesh::class;
    } elseif ($ward === 'miyamae') {
        $modelClass = \App\Models\MiyamaeMesh::class;
    } else {
        return response()->json(['error' => '不正なwardです'], 400);
    }

    $records = $modelClass::all();
    $tagSet = []; // タグ名を保存する連想配列（重複防止のためキーとして使う）

    foreach ($records as $record) {
        // もしpoi_coordsが既に配列ならそのまま使い、文字列ならデコード
        $poiCoords = is_array($record->poi_coords)
            ? $record->poi_coords
            : json_decode($record->poi_coords ?? '', true);

        if (is_array($poiCoords)) {
            foreach ($poiCoords as $name => $coord) {
                if (is_string($name)) {
                    if (
                        $category === 'コンビニ' && (
                            str_contains($name, 'セブン') ||
                            str_contains($name, 'ローソン') ||
                            str_contains($name, 'ファミリーマート')
                        )
                    ) {
                        $tagSet[$name] = true;
                    }

                    if (
                        $category === '病院' && (
                            str_contains($name, '病院') ||
                            str_contains($name, 'クリニック')
                        )
                    ) {
                        $tagSet[$name] = true;
                    }
                }
            }
        }
    }

    return response()->json(array_keys($tagSet), 200, [], JSON_UNESCAPED_UNICODE);
}




    

    // 検索：カテゴリとタグに応じたメッシュ一覧返す
    public function search(Request $request)
    {
        $ward = $request->query('ward');
        $tag = $request->query('tag');

        $model = $ward === 'takatu' ? \App\Models\TakatuMesh::class : \App\Models\MiyamaeMesh::class;
        $records = $model::all();

        $results = [];

        foreach ($records as $record) {
            $coords = $record->poi_coords;
            if (isset($coords[$tag])) {
                $results[] = [
                    'mesh_id' => $record->mesh_id,
                    'coord' => $coords[$tag]
                ];
            }
        }

        return response()->json($results);
    }
}
