<!-- src/components/MeshTagTable.vue -->
<template>
  <div>
    <h2>Mesh Tags</h2>
    <table border="1">
      <thead>
        <tr>
          <th>ID</th>
          <th>Mesh ID</th>
          <th>7-Eleven</th>
          <th>FamilyMart</th>
          <th>Lawson</th>
          <th>Heartful Hospital</th>
          <th>Takatsu Hospital</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="tag in meshTags" :key="tag.id">
          <td>{{ tag.id }}</td>
          <td>{{ tag.mesh_id }}</td>
          <td>{{ tag.seven_eleven }}</td>
          <td>{{ tag.family_mart }}</td>
          <td>{{ tag.lawson }}</td>
          <td>{{ tag.heartful_hospital }}</td>
          <td>{{ tag.takatsu_hospital }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  name: 'MeshTagTable',
  setup() {
    const meshTags = ref([])

    const fetchData = async () => {
      const response = await fetch('http://127.0.0.1:8000/api/mesh-tags')
      const data = await response.json()
      meshTags.value = data
    }

    onMounted(fetchData)

    return { meshTags }
  }
}
</script>
