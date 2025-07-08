<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\File;

class TakatuMeshSeeder extends Seeder
{
    public function run()
    {
        $jsonPath = database_path('seeders/data/poi_mesh_table_with_coords_takatu.json');
        $data = json_decode(File::get($jsonPath), true);

        
        $columns = [
            'seven_eleven',
            'family_mart',
            'lawson',
            'heartful_hospital',
            'takatsu_hospital',
            'kaneko_clinic',
            'bluesky_seikotsuin',
            'medical_scanning_2',
            'kata_kura_hospital',
            'sakado_clinic',
            'teikyo_univ_hospital',
            'mizonokuchi_gastro_clinic',
            'ando_orthopedic',
            'toranomon_branch',
            'takatsu_central_clinic',
        ];

        foreach ($data as $record) {
            $row = [
                'mesh_id' => $record['mesh_id'],
                'poi_coords' => json_encode($record['poi_coords'], JSON_UNESCAPED_UNICODE),
                'created_at' => now(),
                'updated_at' => now(),
            ];

            foreach ($columns as $col) {
                $row[$col] = $record[$this->toOriginalJsonKey($col)] ?? 0;
            }

            DB::table('takatu_mesh')->insert($row);
        }
    }

    
    private function toOriginalJsonKey(string $column): string
    {
        return match ($column) {
            'seven_eleven' => 'セブン-イレブン',
            'family_mart' => 'ファミリーマート',
            'lawson' => 'ローソン',
            'heartful_hospital' => 'ハートフル川崎病院',
            'takatsu_hospital' => '総合高津中央病院',
            'kaneko_clinic' => 'そめや内科クリニック',
            'bluesky_seikotsuin' => 'ブルースカイ整骨院',
            'medical_scanning_2' => 'メディカルスキャニング第二溝の口クリニック',
            'kata_kura_hospital' => '医療法人社団輔仁会片倉病院',
            'sakado_clinic' => '坂戸診療所',
            'teikyo_univ_hospital' => '帝京大学医学部附属溝口病院',
            'mizonokuchi_gastro_clinic' => '溝の口胃腸科・内科クリニック',
            'ando_orthopedic' => '滋恵会安藤整形外科病院',
            'toranomon_branch' => '虎の門病院 分院',
            'takatsu_central_clinic' => '高津中央クリニック',
            default => $column,
        };
    }
}
