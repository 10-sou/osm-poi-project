<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTakatuMeshTable extends Migration
{
    public function up()
    {
        Schema::create('takatu_mesh', function (Blueprint $table) {
            $table->id();
            $table->integer('mesh_id')->unique();
            $table->json('poi_coords'); // POI名 -> [lon, lat]

            // === POIごとの存在有無（boolean） ===
            $table->boolean('seven_eleven')->default(0); // セブン-イレブン
            $table->boolean('family_mart')->default(0); // ファミリーマート
            $table->boolean('lawson')->default(0); // ローソン

            $table->boolean('kaneko_clinic')->default(0); // そめや内科クリニック
            $table->boolean('heartful_hospital')->default(0); // ハートフル川崎病院
            $table->boolean('bluesky_seikotsuin')->default(0); // ブルースカイ整骨院
            $table->boolean('medical_scanning_2')->default(0); // メディカルスキャニング第二溝の口クリニック
            $table->boolean('kata_kura_hospital')->default(0); // 医療法人社団輔仁会片倉病院
            $table->boolean('sakado_clinic')->default(0); // 坂戸診療所
            $table->boolean('teikyo_univ_hospital')->default(0); // 帝京大学医学部附属溝口病院
            $table->boolean('mizonokuchi_gastro_clinic')->default(0); // 溝の口胃腸科・内科クリニック
            $table->boolean('ando_orthopedic')->default(0); // 滋恵会安藤整形外科病院
            $table->boolean('takatsu_hospital')->default(0); // 総合高津中央病院
            $table->boolean('toranomon_branch')->default(0); // 虎の門病院 分院
            $table->boolean('takatsu_central_clinic')->default(0); // 高津中央クリニック

            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('takatu_mesh');
    }
}
