<template>
    <form @submit.prevent="sendMessage" class="flex gap-2 mt-4">
      <input
        v-model="input"
        type="text"
        placeholder="질문을 입력하세요"
        class="flex-1 border rounded px-3 py-2"
      />
      <button class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
        전송
      </button>
    </form>
  </template>
  
  <script>
  export default {
    name: 'ChatInput',
    data() {
      return {
        input: ''
      }
    },
    emits: ['send'],
    methods: {
      sendMessage() {
        if (!this.input.trim()) return
        this.$emit('send', this.input)
        this.input = ''
      }
    }
  }
  </script>
  