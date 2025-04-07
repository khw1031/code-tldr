import uvicorn
from fastapi import FastAPI
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
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)

def start_dev():
  uvicorn.run("app.main:app", host="0.0.0.0", port=15000, reload=True, log_level="debug")

def start_prod():
  uvicorn.run("app.main:app", host="0.0.0.0", port=15000, reload=False, log_level="info")