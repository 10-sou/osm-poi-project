<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class TakatuMesh extends Model
{
    use HasFactory;

    protected $table = 'takatu_mesh';

    protected $fillable = [
        'mesh_id',
        'poi_coords',
        'seven_eleven',
        'family_mart',
        'lawson',
        'heartful_hospital',
        'takatsu_hospital',
    ];

    protected $casts = [
        'poi_coords' => 'array',
        'seven_eleven' => 'boolean',
        'family_mart' => 'boolean',
        'lawson' => 'boolean',
        'heartful_hospital' => 'boolean',
        'takatsu_hospital' => 'boolean',
    ];
}
