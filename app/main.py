from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from . import api

app = FastAPI(
  title="Code TLDR",
  description="Code TLDR",
  version="0.1.0",
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 오리진 허용, 프로덕션에서는 특정 도메인만 허용하는 것이 좋습니다
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

app.include_router(api.router)

def start_dev():
  uvicorn.run("app.main:app", host="0.0.0.0", port=15000, reload=True, log_level="debug")

def start_prod():
  uvicorn.run("app.main:app", host="0.0.0.0", port=15000, reload=False, log_level="info")