<?php

use App\Http\Controllers\Api\MeshTagController;

Route::get('/tag-options', [MeshTagController::class, 'tagOptions']);
Route::get('/search', [MeshTagController::class, 'search']);


Route::get('/mesh-tags', [MeshTagController::class, 'index']);
Route::get('/mesh-tags/{mesh_id}', [MeshTagController::class, 'show']);
