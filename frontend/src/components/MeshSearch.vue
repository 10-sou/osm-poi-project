<template>
  <div>
    <SearchForm
      v-model:selectedWard="selectedWard"
      v-model:selectedCategory="selectedCategory"
      v-model:selectedTag="selectedTag"
      :tagOptions="tagOptions"
      @search="search"
    />

    <SearchResults :results="results" :searched="searched" />

    <MapDisplay :points="results" />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'
import SearchForm from './SearchForm.vue'
import SearchResults from './SearchResults.vue'
import MapDisplay from './MapDisplay.vue'

const selectedWard = ref('')
const selectedCategory = ref('')
const selectedTag = ref('')
const tagOptions = ref([])
const results = ref([])
const searched = ref(false)

// 区やカテゴリの変更でタグオプションを更新
watch([selectedWard, selectedCategory], ([ward, category]) => {
  if (!ward || !category) return

  axios.get(`/api/tag-options?ward=${ward}&category=${category}`)
    .then(res => {
      tagOptions.value = res.data
    })
})

// 検索実行
const search = () => {
  if (!selectedWard.value || !selectedTag.value) return

  const url = `/api/search?ward=${selectedWard.value}&tag=${selectedTag.value}`

  axios.get(url)
    .then(res => {
      const tag = selectedTag.value

      let label = tag
      for (const tagOption of tagOptions.value) {
        if (tagOption.value === tag) {
          label = tagOption.label
          break
        }
      }

      const filtered = []

      for (const row of res.data) {
        const coordsDict = JSON.parse(row.poi_coords)

        filtered.push({
          mesh_id: row.mesh_id,
          coord: coordsDict[label]
        })
      }

      results.value = filtered
      searched.value = true
    })
}

</script>
