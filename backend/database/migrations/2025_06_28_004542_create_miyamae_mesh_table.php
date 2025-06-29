<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateMiyamaeMeshTable extends Migration
{
    public function up()
    {
        Schema::create('miyamae_mesh', function (Blueprint $table) {
            $table->id();
            $table->integer('mesh_id')->unique();
            $table->json('poi_coords'); // tag -> [lon, lat]

            // POI tags (boolean)
            $table->boolean('kaneko_clinic')->default(0);
            $table->boolean('seven_eleven')->default(0);
            $table->boolean('family_mart')->default(0);
            $table->boolean('lawson')->default(0);
            $table->boolean('higashiyoko_hospital')->default(0);      // 一般財団法人 聖マリアンナ会 東横恵愛病院
            $table->boolean('arima_hospital')->default(0);            // 医療法人愛生会有馬病院
            $table->boolean('kawasaki_memorial')->default(0);         // 医療法人花咲会 かわさき記念病院
            $table->boolean('arima_hospital_alt')->default(0);        // 愛生会有馬病院（表記揺れ）
            $table->boolean('higashiyoko_hospital_alt')->default(0);  // 聖マリアンナ会東横恵愛病院（表記揺れ）
            $table->boolean('marianna_university_hospital')->default(0); // 聖マリアンナ医科大学病院

            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('miyamae_mesh');
    }
}
