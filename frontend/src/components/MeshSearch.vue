<template>
  <div>
    <h2>POI メッシュ検索アプリ</h2>

    <SearchForm
      v-model:selectedWard="selectedWard"
      v-model:selectedCategory="selectedCategory"
      v-model:selectedTag="selectedTag"
      :tagOptions="tagOptions"
      @search="search"
    />

    <SearchResults :results="results" :searched="searched" />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'
import SearchForm from './SearchForm.vue'
import SearchResults from './SearchResults.vue'

const selectedWard = ref('takatu')
const selectedCategory = ref('病院')
const selectedTag = ref('')
const tagOptions = ref([])
const results = ref([])
const searched = ref(false)

watch([selectedWard, selectedCategory], async ([ward, category]) => {
  console.log(`🟡 選択変更検知: ward=${ward}, category=${category}`)

  try {
    const response = await axios.get('http://localhost:8000/api/tag-options', {
      params: { ward, category }
    })
    console.log('🟢 APIレスポンス:', response.data)
    tagOptions.value = response.data
    console.log('🟢 tagOptions に格納:', tagOptions.value)
  } catch (error) {
    console.error('🔴 APIエラー:', error)
  }
}, { immediate: true }) // 初回も実行

const search = () => {
  console.log('🔍 検索開始: ', selectedTag.value)
  // 必要に応じて検索処理を追加
}
</script>
