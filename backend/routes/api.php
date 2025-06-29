<?php

use App\Http\Controllers\Api\MeshTagController;

Route::get('/mesh-tags', [MeshTagController::class, 'index']);
Route::get('/mesh-tags/{mesh_id}', [MeshTagController::class, 'show']);
