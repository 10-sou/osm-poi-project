<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\File;

class MiyamaeMeshSeeder extends Seeder
{
    public function run()
    {
        $jsonPath = database_path('seeders/data/poi_mesh_table_with_coords_miyamae.json');
        $json = File::get($jsonPath);
        $records = json_decode($json, true);

        $tagMap = [
            'かねこクリニック' => 'kaneko_clinic',
            'セブン-イレブン' => 'seven_eleven',
            'ファミリーマート' => 'family_mart',
            'ローソン' => 'lawson',
            '一般財団法人　聖マリアンナ会　東横恵愛病院' => 'higashiyoko_hospital',
            '医療法人愛生会有馬病院' => 'arima_hospital',
            '医療法人花咲会　かわさき記念病院' => 'kawasaki_memorial',
            '愛生会有馬病院' => 'arima_hospital_alt',
            '聖マリアンナ会東横恵愛病院' => 'higashiyoko_hospital_alt',
            '聖マリアンナ医科大学病院' => 'marianna_university_hospital',
        ];

        foreach ($records as $record) {
            $row = [
                'mesh_id' => $record['mesh_id'],
                'poi_coords' => json_encode($record['poi_coords']),
            ];

            
            foreach ($tagMap as $jp => $en) {
                $row[$en] = isset($record[$jp]) ? $record[$jp] : 0;
            }

            DB::table('miyamae_mesh')->insert($row);
        }
    }
}
