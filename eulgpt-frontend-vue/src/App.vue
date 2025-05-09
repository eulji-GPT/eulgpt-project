<template>
  <div class="max-w-2xl mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">💬 을GPT 챗봇</h1>

    <div class="h-[400px] overflow-y-auto border p-4 rounded bg-white shadow">
      <ChatMessage
        v-for="(msg, index) in messages"
        :key="index"
        :message="msg"
      />
    </div>

    <ChatInput @send="handleUserMessage" />
  </div>
</template>

<script>
import axios from 'axios'
import ChatMessage from './components/ChatMessage.vue'
import ChatInput from './components/ChatInput.vue'

export default {
  components: {
    ChatMessage,
    ChatInput
  },
  data() {
    return {
      messages: []
    }
  },
  methods: {
    async handleUserMessage(text) {
      this.messages.push({ role: 'user', content: text })

      try {
        const res = await axios.post('http://localhost:8000/api/chat', {
          message: text
        })
        this.messages.push({ role: 'ai', content: res.data.answer })
      } catch (err) {
        this.messages.push({ role: 'ai', content: '[오류] 응답을 불러오지 못했습니다.' })
      }
    }
  }
}
</script>
