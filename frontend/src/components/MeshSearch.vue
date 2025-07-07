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
watch([selectedWard, selectedCategory], async ([ward, category]) => {
  console.log('🟡 選択変更検知: ward=', ward, 'category=', category)
  if (!ward || !category) return

  try {
    const res = await axios.get(`/api/tag-options?ward=${ward}&category=${category}`)
    console.log('🟢 APIレスポンス受信:', res.data)
    tagOptions.value = res.data
  } catch (error) {
    console.error('🔴 タグオプション取得エラー:', error)
  }
})

// 検索実行
const search = async () => {
  if (!selectedWard.value || !selectedTag.value) return

  const url = `/api/search?ward=${selectedWard.value}&tag=${selectedTag.value}`
  console.log('🔍 検索実行:', url)

  try {
    const res = await axios.get(url)
    const tag = selectedTag.value
    const label = tagOptions.value.find(opt => opt.value === tag)?.label ?? tag

    const filtered = []

    for (const row of res.data) {
      if (row.poi_coords) {
        try {
          const coordsDict = JSON.parse(row.poi_coords)
          if (coordsDict.hasOwnProperty(label)) {
            filtered.push({
              mesh_id: row.mesh_id,
              coord: coordsDict[label]
            })
          }
        } catch (e) {
          console.warn("⚠️ JSONパース失敗:", row.poi_coords)
        }
      }
    }

    console.log('✅ フィルタ後の検索結果:', filtered)

    results.value = filtered
    searched.value = true
  } catch (error) {
    console.error("検索エラー:", error)
    results.value = []
    searched.value = true
  }
}
</script>
