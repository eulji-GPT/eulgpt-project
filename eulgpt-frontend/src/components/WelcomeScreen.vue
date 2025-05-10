<template>
  <div class="chatgpt-container">
    <!-- 상단 헤더 -->
    <header class="top-bar">
      <span class="logo">ChatGPT 4o</span>
      <div class="top-right">
        <button class="btn-temp">임시</button>
        <div class="profile-icon">P<br />PLUS</div>
      </div>
    </header>

    <!-- 중앙 인사말 -->
    <main class="main-message">
      <p><strong>UCHAN</strong> 님, 어서 와요. 시작할 준비 되셨나요?</p>
    </main>

    <!-- 하단 입력창 -->
    <footer class="input-area">
      <input type="text" placeholder="무엇이든 물어보세요" />
      <div class="input-buttons">
        <button>🔍 검색</button>
        <button>📚 심층 리서치</button>
        <button>🎨 이미지 그리기</button>
        <button>🎤</button>
        <button>📶</button>
      </div>
    </footer>
  </div>
</template>

<script setup>
// 별도 로직 없음
</script>

<style scoped>
.chatgpt-container {
  font-family: "Arial", sans-serif;
  padding: 20px;
}

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-weight: bold;
}

.top-right {
  display: flex;
  gap: 10px;
  align-items: center;
}

.btn-temp {
  background-color: #eee;
  border: none;
  padding: 5px 10px;
}

.profile-icon {
  background-color: #007aff;
  color: white;
  padding: 5px;
  border-radius: 50%;
  text-align: center;
  font-size: 12px;
  width: 30px;
  height: 30px;
  line-height: 15px;
}

.main-message {
  text-align: center;
  margin: 100px 0;
  font-size: 20px;
}

.input-area {
  border: 1px solid #ccc;
  border-radius: 20px;
  padding: 10px;
  display: flex;
  flex-direction: column;
}

.input-area input {
  border: none;
  outline: none;
  font-size: 16px;
  margin-bottom: 10px;
}

.input-buttons {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
</style>
