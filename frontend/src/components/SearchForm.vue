<template>
  <div>
    <label>対象区:</label>
    <select :value="selectedWard" @change="onWardChange">
      <option disabled value="">区を選んでください</option>
      <option value="takatuki">高津区</option>
      <option value="miyamae">宮前区</option>
    </select>

    <div v-if="tagOptions.length > 0">
      <label>タグ:</label>
      <select :value="selectedTag" @change="onTagChange">
        <option disabled value="">タグを選んでください</option>
        <option v-for="tag in tagOptions" :key="tag" :value="tag">{{ tag }}</option>
      </select>
      <button @click="emitSearch">検索</button>
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
  emits: ['update:selectedWard', 'update:selectedTag', 'search'],
  methods: {
    onWardChange(event) {
      this.$emit('update:selectedWard', event.target.value)
    },
    onTagChange(event) {
      this.$emit('update:selectedTag', event.target.value)
    },
    emitSearch() {
      this.$emit('search')
    }
  }
}
</script>
