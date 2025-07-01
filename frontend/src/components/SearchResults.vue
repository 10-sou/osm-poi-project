<!-- components/SearchResults.vue -->
<template>
  <div>
    <div v-if="results.length > 0">
      <h3>該当メッシュIDとPOI座標:</h3>
      <table>
        <thead>
          <tr>
            <th>メッシュID</th>
            <th>緯度</th>
            <th>経度</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="result in results" :key="result.mesh_id">
            <td>{{ result.mesh_id }}</td>
            <td>{{ result.coord[1] }}</td>
            <td>{{ result.coord[0] }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else-if="searched">
      <p>該当なし</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchResults',
  props: {
    results: Array,
    searched: Boolean
  }
}
</script>
