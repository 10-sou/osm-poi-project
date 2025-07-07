<template>
  <div>
    <label>対象区:</label>
    <select :value="selectedWard" @change="onWardChange">
      <option disabled value="">区を選んでください</option>
      <option value="takatu">高津区</option>
      <option value="miyamae">宮前区</option>
    </select>

    <label>カテゴリ:</label>
    <select :value="selectedCategory" @change="onCategoryChange">
      <option disabled value="">カテゴリを選んでください</option>
      <option value="病院">病院</option>
      <option value="コンビニ">コンビニ</option>
    </select>

    <label>タグ:</label>
    <select :value="selectedTag" @change="onTagChange">
      <option disabled value="">タグを選んでください</option>
      <option
        v-for="option in tagOptions"
        :key="option.value"
        :value="option.value"
      >
        {{ option.label }}
      </option>
    </select>

    <button @click="$emit('search')">検索</button>
  </div>
</template>

<script setup>
const props = defineProps({
  selectedWard: String,
  selectedCategory: String,
  selectedTag: String,
  tagOptions: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits([
  'update:selectedWard',
  'update:selectedCategory',
  'update:selectedTag',
  'search'
])

const onWardChange = (e) => {
  console.log('🟡 区変更 emit:', e.target.value)
  emit('update:selectedWard', e.target.value)
}

const onCategoryChange = (e) => {
  console.log('🟡 カテゴリ変更 emit:', e.target.value)
  emit('update:selectedCategory', e.target.value)
}

const onTagChange = (e) => {
  console.log('🟡 タグ変更 emit:', e.target.value)
  emit('update:selectedTag', e.target.value)
}
</script>
