<template>
  <div>
    <h2>POI メッシュ検索アプリ</h2>
    <h3>タグでメッシュIDを検索</h3>

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

<script>
import { ref, onMounted, watch } from 'vue'
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
    const selectedCategory = ref('病院')
    const selectedTag = ref('')
    const tagOptions = ref([])
    const results = ref([])
    const searched = ref(false)

    const fetchTagOptions = async () => {
      if (selectedWard.value && selectedCategory.value) {
        const url = `http://localhost:8000/api/tag-options?ward=${selectedWard.value}&category=${selectedCategory.value}`
        console.log("🔍 APIリクエストURL:", url)

        try {
          const res = await axios.get(url)
          console.log("📦 受信したres.data:", res.data)
          console.log("📦 typeof res.data:", typeof res.data)

          if (typeof res.data === 'string') {
            try {
              const parsed = JSON.parse(res.data)
              console.log("✅ JSON.parse 成功:", parsed)
              tagOptions.value = Array.isArray(parsed) ? parsed : []
            } catch (e) {
              console.error("❌ JSONパース失敗:", e)
              tagOptions.value = []
            }
          } else if (Array.isArray(res.data)) {
            console.log("✅ 配列として受信:", res.data)
            tagOptions.value = res.data
          } else {
            console.warn("⚠️ 想定外の形式:", res.data)
            tagOptions.value = []
          }
        } catch (error) {
          console.error("❌ APIエラー:", error)
        }
      }
    }

    watch([selectedWard, selectedCategory], () => {
      console.log("🔄 watch発火: ward or categoryが変更されました")
      fetchTagOptions()
    })

    onMounted(() => {
      console.log("🚀 onMounted: 初期タグ取得")
      fetchTagOptions()
    })

    const search = async () => {
      console.log("🔎 検索実行: 選択されたタグ", selectedTag.value)

      if (!selectedTag.value) {
        console.warn("⚠️ タグが選択されていません")
        return
      }

      try {
        const url = `http://localhost:8000/api/search?ward=${selectedWard.value}&tag=${selectedTag.value}`
        console.log("🔍 検索リクエストURL:", url)
        const res = await axios.get(url)
        results.value = res.data
        searched.value = true
        console.log("📦 検索結果:", results.value)
      } catch (error) {
        console.error("❌ 検索エラー:", error)
      }
    }

    return {
      selectedWard,
      selectedCategory,
      selectedTag,
      tagOptions,
      results,
      searched,
      search
    }
  }
}
</script>
