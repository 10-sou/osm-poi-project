<template>
  <div>
    <label>対象区:</label>
    <select v-model="localWard" @change="onWardChange">
      <option disabled value="">区を選んでください</option>
      <option value="takatuki">高津区</option>
      <option value="miyamae">宮前区</option>
    </select>

    <label>カテゴリ:</label>
    <select v-model="localCategory" @change="onCategoryChange">
      <option disabled value="">カテゴリを選んでください</option>
      <option value="病院">病院</option>
      <option value="コンビニ">コンビニ</option>
    </select>

    <div v-if="tagOptions.length > 0">
      <label>タグ:</label>
      <select v-model="localTag" @change="onTagChange">
        <option disabled value="">タグを選んでください</option>
        <option v-for="tag in tagOptions" :key="tag" :value="tag">{{ tag }}</option>
      </select>
    </div>

    <button @click="emitSearch">検索</button>
  </div>
</template>

<script>
import { ref, watch, onMounted } from 'vue'

export default {
  name: 'SearchForm',
  props: {
    selectedWard: String,
    selectedCategory: String,
    selectedTag: String,
    tagOptions: Array
  },
  emits: ['update:selectedWard', 'update:selectedCategory', 'update:selectedTag', 'search'],
  setup(props, { emit }) {
    const localWard = ref(props.selectedWard || '')
    const localCategory = ref(props.selectedCategory || '')
    const localTag = ref(props.selectedTag || '')

    // 初期表示ログ
    onMounted(() => {
      console.log("📦 SearchForm mounted")
      console.log("  ▶ 初期 ward:", localWard.value)
      console.log("  ▶ 初期 category:", localCategory.value)
      console.log("  ▶ 初期 tag:", localTag.value)
    })

    const onWardChange = () => {
      console.log("🌀 Ward 選択:", localWard.value)
      emit('update:selectedWard', localWard.value)
    }

    const onCategoryChange = () => {
      console.log("🌀 Category 選択:", localCategory.value)
      emit('update:selectedCategory', localCategory.value)
    }

    const onTagChange = () => {
      console.log("🌀 Tag 選択:", localTag.value)
      emit('update:selectedTag', localTag.value)
    }

    const emitSearch = () => {
      console.log("🔍 検索ボタンクリック")
      emit('search')
    }

    watch(() => props.tagOptions, (newTags) => {
      console.log("📥 props.tagOptions 更新:", newTags)
    })

    return {
      localWard,
      localCategory,
      localTag,
      onWardChange,
      onCategoryChange,
      onTagChange,
      emitSearch
    }
  }
}
</script>
