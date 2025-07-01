<!-- components/SearchForm.vue -->
<template>
  <div>
    <label>対象区:</label>
    <select v-model="selectedWard" @change="$emit('ward-change', selectedWard)">
      <option disabled value="">区を選んでください</option>
      <option value="takatuki">高津区</option>
      <option value="miyamae">宮前区</option>
    </select>

    <div v-if="tagOptions.length > 0">
      <label>タグ:</label>
      <select v-model="selectedTag">
        <option disabled value="">タグを選んでください</option>
        <option v-for="tag in tagOptions" :key="tag" :value="tag">{{ tag }}</option>
      </select>
      <button @click="$emit('search', selectedTag)">検索</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchForm',
  props: {
    selectedWard: String,
    selectedTag: String,
    tagOptions: Array
  },
  emits: ['ward-change', 'search']
}
</script>
