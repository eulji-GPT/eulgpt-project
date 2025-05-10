from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router
from app.config.settings import settings

app = FastAPI(
    title="EulGPT Backend API",
    description="모노레포 기반 FastAPI 백엔드 서버",
    version="1.0.0"
)

# CORS 설정 (프론트엔드에서 호출 가능하도록)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 연결
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Welcome to EulGPT Backend"}
