<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
  public function up(): void
{
    Schema::create('mesh_tags', function (Blueprint $table) {
        $table->id();
        $table->unsignedBigInteger('mesh_id')->index();

        // タグ名が日本語なので、列名は英語にマッピングする（例）
        $table->float('seven_eleven')->default(0);
        $table->float('family_mart')->default(0);
        $table->float('lawson')->default(0);
        $table->float('heartful_hospital')->default(0);
        $table->float('takatsu_hospital')->default(0);

        $table->timestamps();
    });
}

};
