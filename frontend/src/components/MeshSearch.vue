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
const selectedCategory = ref('コンビニ')
const selectedTag = ref('')
const tagOptions = ref([])
const results = ref([])
const searched = ref(false)

const fetchTags = async () => {
  try {
    const response = await axios.get('/api/tag-options', {
      params: {
        ward: selectedWard.value,
        category: selectedCategory.value
      }
    })
    tagOptions.value = response.data
  } catch (error) {
    console.error('タグの取得に失敗しました', error)
    tagOptions.value = []
  }
}

const search = async () => {
  try {
    const response = await axios.get('/api/search', {
      params: {
        ward: selectedWard.value,
        tag: selectedTag.value
      }
    })
    results.value = response.data
    searched.value = true
  } catch (error) {
    console.error('検索に失敗しました', error)
    results.value = []
    searched.value = false
  }
}

watch([selectedWard, selectedCategory], fetchTags, { immediate: true })
</script>
