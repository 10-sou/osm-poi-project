<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;

class MeshTagController extends Controller
{
    public function index(Request $request)
    {
        $ward = $request->query('ward', 'takatuki');

        $tableMap = [
            'takatuki' => 'takatu_mesh',
            'miyamae' => 'miyamae_mesh',
        ];

        if (!array_key_exists($ward, $tableMap)) {
            return response()->json(['error' => 'Invalid ward'], 400);
        }

        $data = DB::table($tableMap[$ward])->get();

        return response()->json($data);
    }

    public function show($mesh_id, Request $request)
    {
        $ward = $request->query('ward', 'takatuki');

        $tableMap = [
            'takatuki' => 'takatu_mesh',
            'miyamae' => 'miyamae_mesh',
        ];

        if (!array_key_exists($ward, $tableMap)) {
            return response()->json(['error' => 'Invalid ward'], 400);
        }

        $record = DB::table($tableMap[$ward])->where('mesh_id', $mesh_id)->first();
        return response()->json($record);
    }
}
