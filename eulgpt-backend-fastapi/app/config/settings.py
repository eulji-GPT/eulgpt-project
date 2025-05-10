from pydantic_settings import BaseSettings 
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "EulGPT Backend"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]  # 프론트엔드 주소
    DATABASE_URL: str = "sqlite:///./test.db"  # 추후 PostgreSQL 등으로 변경 가능

    class Config:
        env_file = ".env"

settings = Settings()
