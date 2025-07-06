<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class MeshTagController extends Controller
{
    public function tagOptions(Request $request)
    {
        $ward = $request->query('ward');
        $category = $request->query('category');

        // 区ごとのカテゴリとタグ
        $categoryTagMap = [
            'takatu' => [
                '病院' => [
                    'kaneko_clinic',
                    'arima_hospital',
                    'arima_hospital_alt',
                    'kawasaki_memorial',
                    'higashiyoko_hospital',
                    'higashiyoko_hospital_alt',
                    'marianna_university_hospital',
                    'heartful_hospital',
                    'takatsu_hospital',
                    'bluesky_seikotsuin',
                    'medical_scanning_2',
                    'kata_kura_hospital',
                    'sakado_clinic',
                    'teikyo_univ_hospital',
                    'mizonokuchi_gastro_clinic',
                    'ando_orthopedic',
                    'toranomon_branch',
                    'takatsu_central_clinic',
                ],
                'コンビニ' => [
                    'seven_eleven',
                    'family_mart',
                    'lawson',
                ],
            ],
            'miyamae' => [
                '病院' => [
                    'kaneko_clinic',
                    'arima_hospital',
                    'arima_hospital_alt',
                    'kawasaki_memorial',
                    'higashiyoko_hospital',
                    'higashiyoko_hospital_alt',
                    'marianna_university_hospital',
                ],
                'コンビニ' => [
                    'seven_eleven',
                    'family_mart',
                    'lawson',
                ],
            ],
        ];

        $labelMap = [
            'kaneko_clinic' => 'かねこクリニック',
            'arima_hospital' => '医療法人愛生会有馬病院',
            'arima_hospital_alt' => '愛生会有馬病院',
            'kawasaki_memorial' => '医療法人花咲会　かわさき記念病院',
            'higashiyoko_hospital' => '一般財団法人　聖マリアンナ会　東横恵愛病院',
            'higashiyoko_hospital_alt' => '聖マリアンナ会東横恵愛病院',
            'marianna_university_hospital' => '聖マリアンナ医科大学病院',
            'seven_eleven' => 'セブン-イレブン',
            'family_mart' => 'ファミリーマート',
            'lawson' => 'ローソン',

            // 高津区追加病院名
            'heartful_hospital' => 'ハートフル川崎病院',
            'takatsu_hospital' => '総合高津中央病院',
            'bluesky_seikotsuin' => 'ブルースカイ整骨院',
            'medical_scanning_2' => 'メディカルスキャニング第二溝の口クリニック',
            'kata_kura_hospital' => '医療法人社団輔仁会片倉病院',
            'sakado_clinic' => '坂戸診療所',
            'teikyo_univ_hospital' => '帝京大学医学部附属溝口病院',
            'mizonokuchi_gastro_clinic' => '溝の口胃腸科・内科クリニック',
            'ando_orthopedic' => '滋恵会安藤整形外科病院',
            'toranomon_branch' => '虎の門病院 分院',
            'takatsu_central_clinic' => '高津中央クリニック',
        ];

        $values = $categoryTagMap[$ward][$category] ?? [];

        $tags = [];

        foreach ($values as $value) {
            $label = $labelMap[$value] ?? $value;
            $tags[] = [
                'value' => $value,
                'label' => $label,
            ];
        }

        return response()->json($tags, 200, [], JSON_UNESCAPED_UNICODE);
    }
}
