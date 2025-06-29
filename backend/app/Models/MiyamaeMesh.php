<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class MiyamaeMesh extends Model
{
    use HasFactory;

    protected $table = 'miyamae_mesh';

    protected $fillable = [
        'mesh_id',
        'poi_coords',
        'kaneko_clinic',
        'seven_eleven',
        'family_mart',
        'lawson',
        'higashiyoko_hospital',
        'arima_hospital',
        'kawasaki_memorial',
        'arima_hospital_alt',
        'higashiyoko_hospital_alt',
        'marianna_university_hospital',
    ];

    protected $casts = [
        'poi_coords' => 'array',
        'kaneko_clinic' => 'boolean',
        'seven_eleven' => 'boolean',
        'family_mart' => 'boolean',
        'lawson' => 'boolean',
        'higashiyoko_hospital' => 'boolean',
        'arima_hospital' => 'boolean',
        'kawasaki_memorial' => 'boolean',
        'arima_hospital_alt' => 'boolean',
        'higashiyoko_hospital_alt' => 'boolean',
        'marianna_university_hospital' => 'boolean',
    ];
}
