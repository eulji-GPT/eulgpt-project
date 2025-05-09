<template>
    <div :class="message.role === 'user' ? 'text-right' : 'text-left'">
      <div
        :class="[
          'inline-block px-4 py-2 my-2 rounded-lg max-w-[80%]',
          message.role === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-black'
        ]"
      >
        {{ message.content }}
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ChatMessage',
    props: {
      message: {
        type: Object,
        required: true
      }
    }
  }
  </script>
  