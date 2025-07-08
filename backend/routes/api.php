<?php

use App\Http\Controllers\Api\MeshTagController;

Route::get('/tag-options', [MeshTagController::class, 'tagOptions']);
Route::get('/search', [MeshTagController::class, 'search']);



