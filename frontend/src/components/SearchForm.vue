<template>
  <div>
    対象区:
    <select v-model="localWard" @change="emitWard">
      <option value="takatuki">高津区</option>
      <option value="miyamae">宮前区</option>
    </select>

    カテゴリ:
    <select v-model="localCategory" @change="emitCategory">
      <option value="コンビニ">コンビニ</option>
      <option value="病院">病院</option>
    </select>

    タグ:
    <select v-model="localTag">
      <option disabled value="">タグを選んでください</option>
      <option v-for="tag in tagOptions" :key="tag" :value="tag">{{ tag }}</option>
    </select>

    <button @click="emitSearch">検索</button>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useEmit } from 'vue'

const emit = defineEmits(['update:selectedWard', 'update:selectedCategory', 'update:selectedTag', 'search'])

const props = defineProps({
  selectedWard: String,
  selectedCategory: String,
  selectedTag: String,
  tagOptions: Array
})

const localWard = ref(props.selectedWard)
const localCategory = ref(props.selectedCategory)
const localTag = ref(props.selectedTag)

const emitWard = () => {
  emit('update:selectedWard', localWard.value)
}
const emitCategory = () => {
  emit('update:selectedCategory', localCategory.value)
}
const emitSearch = () => {
  emit('update:selectedTag', localTag.value)
  emit('search')
}
</script>
