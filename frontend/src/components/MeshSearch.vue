<template>
  <div>
    <h2>POI メッシュ検索アプリ</h2>
    <h3>タグでメッシュIDを検索</h3>

    <SearchForm
      v-model:selectedWard="selectedWard"
      v-model:selectedTag="selectedTag"
      :tagOptions="tagOptions"
      @search="search"
    />

    <SearchResults :results="results" :searched="searched" />

    <!-- 🔽 新たに地図表示コンポーネント追加 -->
    <MapDisplay :points="results" />
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'
import SearchForm from './SearchForm.vue'
import SearchResults from './SearchResults.vue'
import MapDisplay from './MapDisplay.vue' // 追加

export default {
  name: 'MeshSearch',
  components: {
    SearchForm,
    SearchResults,
    MapDisplay // 追加
  },
  setup() {
    const selectedWard = ref('takatuki')
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

    onMounted(fetchData)
    watch(selectedWard, fetchData)

    return {
      selectedWard,
      selectedTag,
      tagOptions,
      results,
      searched,
      search
    }
  }
}
</script>
