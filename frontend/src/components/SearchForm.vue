<template>
  <div>
    <label>対象区:</label>
    <select v-model="localWard" @change="onWardChange">
      <option disabled value="">区を選んでください</option>
      <option value="takatu">高津区</option>
      <option value="miyamae">宮前区</option>
    </select>

    <label>カテゴリ:</label>
    <select v-model="localCategory" @change="onCategoryChange">
      <option disabled value="">カテゴリを選んでください</option>
      <option value="病院">病院</option>
      <option value="コンビニ">コンビニ</option>
    </select>

    <label>タグ:</label>
    <select v-model="localTag">
      <option disabled value="">タグを選んでください</option>
      <option
        v-for="option in tagOptions"
        :key="option.value"
        :value="option.value"
      >
        {{ option.label }}
      </option>
    </select>

    <button @click="search">検索</button>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  selectedWard: String,
  selectedCategory: String,
  selectedTag: String,
  tagOptions: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits(['update:selectedWard', 'update:selectedCategory', 'update:selectedTag', 'search'])

const localWard = ref(props.selectedWard)
const localCategory = ref(props.selectedCategory)
const localTag = ref(props.selectedTag)

watch(() => props.selectedWard, (newVal) => localWard.value = newVal)
watch(() => props.selectedCategory, (newVal) => localCategory.value = newVal)
watch(() => props.selectedTag, (newVal) => localTag.value = newVal)

watch(() => props.tagOptions, (val) => {
  console.log("🟢 SearchForm.vue: tagOptions を受け取りました:", val)
})

const onWardChange = () => emit('update:selectedWard', localWard.value)
const onCategoryChange = () => emit('update:selectedCategory', localCategory.value)

watch(localTag, (val) => emit('update:selectedTag', val))

const search = () => emit('search')
</script>
