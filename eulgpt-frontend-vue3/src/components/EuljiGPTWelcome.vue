<template>
  <div class="eulji-container">
    <!-- 상단 헤더 -->
    <header class="header">
      <div class="logo">🎓 Eulji GPT</div>
      <div class="profile">
        <button class="btn-mode">베타</button>
        <div class="circle">U</div>
      </div>
    </header>

    <!-- 중앙 인사말 -->
    <main class="greeting">
      <h1>UCHAN 님,</h1>
      <p><strong>Eulji GPT</strong>에 오신 걸 환영합니다!</p>
      <p class="sub">오늘은 어떤 도움이 필요하신가요?</p>
    </main>

    <!-- 입력창 영역 -->
    <footer class="input-box">
      <input type="text" placeholder="무엇이든 입력해 보세요" />
      <div class="tools">
        <button><span>🔍</span> 검색</button>
        <button><span>📘</span> 자료 분석</button>
        <button><span>🎨</span> 이미지 생성</button>
        <button><span>🎤</span> 음성 입력</button>
        <button><span>🧠</span> 학습 도우미</button>
      </div>
    </footer>
  </div>
</template>

<script setup>
// 특별한 로직 없음
</script>

<style scoped>
.eulji-container {
  font-family: 'Segoe UI', sans-serif;
  padding: 30px;
  background: #fdfdfc;
  color: #222;
  min-height: 100vh;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-weight: bold;
  font-size: 20px;
}

.profile {
  display: flex;
  gap: 10px;
  align-items: center;
}

.btn-mode {
  background: #ffdb99;
  border: none;
  padding: 5px 10px;
  border-radius: 8px;
  font-size: 12px;
  font-weight: bold;
}

.circle {
  background-color: #5a9bd4;
  color: white;
  font-weight: bold;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  text-align: center;
  line-height: 30px;
}

.greeting {
  text-align: center;
  margin: 80px 0 40px;
}

.greeting h1 {
  font-size: 28px;
  margin-bottom: 10px;
}

.greeting .sub {
  color: #555;
  font-size: 16px;
}

.input-box {
  border: 1px solid #ccc;
  border-radius: 20px;
  padding: 15px;
  background: white;
}

.input-box input {
  border: none;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  outline: none;
}

.tools {
  margin-top: 15px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
}

.tools button {
  background: #eef2f5;
  border: none;
  padding: 8px 12px;
  border-radius: 12px;
  font-size: 14px;
  display: flex;
  gap: 6px;
  align-items: center;
  transition: 0.2s;
}

.tools button:hover {
  background: #d7e9f7;
}
</style>
