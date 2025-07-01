<template>
  <div>
    <h2>POI メッシュ検索アプリ</h2>
    <h3>タグでメッシュIDを検索</h3>

    <SearchForm
      :selectedWard="selectedWard"
      :selectedTag="selectedTag"
      :tagOptions="tagOptions"
      @ward-change="handleWardChange"
      @search="search"
    />

    <SearchResults :results="results" :searched="searched" />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import SearchForm from './SearchForm.vue'
import SearchResults from './SearchResults.vue'

export default {
  name: 'MeshSearch',
  components: {
    SearchForm,
    SearchResults
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

    const handleWardChange = (ward) => {
      selectedWard.value = ward
      fetchData()
    }

    const search = (tag) => {
      selectedTag.value = tag
      results.value = []
      searched.value = true

      for (const row of allData.value) {
        if (row.poi_coords) {
          try {
            const coordsDict = JSON.parse(row.poi_coords)
            const coord = coordsDict[tag]
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

    return {
      selectedWard,
      selectedTag,
      tagOptions,
      results,
      searched,
      handleWardChange,
      search
    }
  }
}
</script>
