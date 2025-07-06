<template>
  <div v-if="searched">
    <h3>検索結果</h3>
    <ul>
      <li v-for="(item, index) in results" :key="index">
        メッシュID: {{ item.mesh_id }} - 座標: {{ item.coord[0] }}, {{ item.coord[1] }}
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  results: Array,
  searched: Boolean
})
</script>
