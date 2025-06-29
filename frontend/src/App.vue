<template>
  <div>
    <h1>POI メッシュ検索アプリ</h1>
    <MeshSearch />
  </div>
</template>

<script>
import MeshSearch from './components/MeshSearch.vue'

export default {
  components: {
    MeshSearch
  }
}
</script>

<style>
h1 {
  font-size: 24px;
  margin: 20px 0;
  text-align: center;
}
</style>
