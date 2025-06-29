<?php

namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class PoiMeshMiyamaeController extends Controller
{
    public function index()
    {
        return DB::table('mesh_tags_miyamae')->get();
    }
}
