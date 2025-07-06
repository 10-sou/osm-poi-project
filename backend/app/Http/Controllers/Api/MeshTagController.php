<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

class MeshTagController extends Controller
{
    public function tagOptions(Request $request)
    {
        // 🔍 受け取ったパラメータをログ出力
        $ward = $request->query('ward');
        $category = $request->query('category');
        Log::info('📝 tagOptions() called', ['ward' => $ward, 'category' => $category]);

        // 🔍 受け取れていない場合のエラー処理（400）
        if (!$ward || !$category) {
            Log::warning('❌ パラメータが不足しています', ['ward' => $ward, 'category' => $category]);
            return response()->json(['error' => 'Missing ward or category'], 400);
        }

        // ✅ テストデータで仮の動作確認（本来はDB処理など）
        $mockData = [
            '病院' => ['虎の門病院 分院', 'ハートフル川崎病院'],
            'コンビニ' => ['セブン-イレブン', 'ファミリーマート', 'ローソン']
        ];

        $tags = $mockData[$category] ?? [];

        // 🔍 返却値のログ
        Log::info('✅ 返却タグ一覧', ['tags' => $tags]);

        return response()->json($tags, 200, [], JSON_UNESCAPED_UNICODE);
    }
}
