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

const selectedWard = ref('miyamae')
const selectedCategory = ref('病院')
const selectedTag = ref('')
const tagOptions = ref([])
const results = ref([])
const searched = ref(false)

// ✅ APIのURLをLaravelに向ける（http://localhost:8000）
// ✅ CORS確認用ログも含めて
watch([selectedWard, selectedCategory], async ([ward, category]) => {
  if (!ward || !category) return

  console.log(`🟡 選択変更検知: ward=${ward}, category=${category}`)
  try {
    const url = `http://localhost:8000/api/tag-options?ward=${ward}&category=${category}`
    console.log('🔄 APIリクエスト送信先:', url)

    const response = await axios.get(url)
    console.log('🟢 APIレスポンス受信:', response.data)

    if (Array.isArray(response.data)) {
      tagOptions.value = response.data
    } else {
      console.warn('⚠️ 受信したデータは配列ではありません:', response.data)
      tagOptions.value = []
    }
  } catch (error) {
    console.error('🔴 APIエラー発生:', error)
    if (error.response) {
      console.error('🔴 レスポンスステータス:', error.response.status)
      console.error('🔴 レスポンスデータ:', error.response.data)
    } else if (error.request) {
      console.error('🔴 リクエストは送信されたが応答なし（CORSの可能性）:', error.request)
    } else {
      console.error('🔴 リクエスト設定時のエラー:', error.message)
    }
  }
}, { immediate: true })

function search() {
  console.log(`🔍 検索実行: ward=${selectedWard.value}, tag=${selectedTag.value}`)
  searched.value = true
}
</script>
