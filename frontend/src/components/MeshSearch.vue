<template>
  <div>
    <h2>POI メッシュ検索アプリ</h2>
    <h3>タグでメッシュIDを検索</h3>

    <!-- 対象区選択 -->
    <label>対象区:</label>
    <select v-model="selectedWard" @change="fetchData">
      <option disabled value="">区を選んでください</option>
      <option value="takatuki">高津区</option>
      <option value="miyamae">宮前区</option>
    </select>

    <!-- タグ選択 -->
    <div v-if="tagOptions.length > 0">
      <label>タグ:</label>
      <select v-model="selectedTag">
        <option disabled value="">タグを選んでください</option>
        <option v-for="tag in tagOptions" :key="tag" :value="tag">{{ tag }}</option>
      </select>
      <button @click="search">検索</button>
    </div>

    <!-- 検索結果表示 -->
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
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'MeshSearch',
  setup() {
    const selectedWard = ref('')
    const selectedTag = ref('')
    const tagOptions = ref([])
    const allData = ref([])
    const results = ref([])
    const searched = ref(false)

    const fetchData = async () => {
      if (!selectedWard.value) return
      try {
        const url = `http://127.0.0.1:8000/api/mesh-tags?ward=${selectedWard.value}`
        const res = await axios.get(url)
        allData.value = res.data
        selectedTag.value = ''
        results.value = []
        searched.value = false

        const tagSet = new Set()

        for (const row of res.data) {
          if (row.poi_coords) {
            try {
              const coordsDict = JSON.parse(row.poi_coords)
              Object.keys(coordsDict).forEach(tag => tagSet.add(tag))
            } catch (e) {
              console.warn("JSONパース失敗", row.poi_coords)
            }
          }
        }

        tagOptions.value = Array.from(tagSet)

      } catch (error) {
        console.error('API読み込み失敗:', error)
      }
    }

    const search = () => {
      results.value = []
      searched.value = true

      if (!selectedTag.value) return

      for (const row of allData.value) {
        if (row.poi_coords) {
          try {
            const coordsDict = JSON.parse(row.poi_coords)
            const coord = coordsDict[selectedTag.value]
            if (coord) {
              results.value.push({
                mesh_id: row.mesh_id,
                coord: coord
              })
            }
          } catch (e) {
            console.warn("JSONパース失敗", row.poi_coords)
          }
        }
      }
    }

    onMounted(() => {
      selectedWard.value = 'takatuki'
      fetchData()
    })

    return {
      selectedWard,
      selectedTag,
      tagOptions,
      results,
      fetchData,
      search,
      searched
    }
  }
}
</script>

<style scoped>
label {
  display: block;
  margin-top: 10px;
}
select {
  margin-right: 10px;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}
th, td {
  border: 1px solid #ccc;
  padding: 6px;
  text-align: center;
}
</style>
