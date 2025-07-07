<template>
  <div v-if="searched">
    <h3>検索結果</h3>
    <table border="1" cellpadding="5">
      <thead>
        <tr>
          <th>メッシュID</th>
          <th>経度 (Longitude)</th>
          <th>緯度 (Latitude)</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in results" :key="index">
          <td>{{ item.mesh_id }}</td>
          <td>{{ item.coord?.[0] ?? '不明' }}</td>
          <td>{{ item.coord?.[1] ?? '不明' }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
defineProps({
  results: Array,
  searched: Boolean
})
</script>
