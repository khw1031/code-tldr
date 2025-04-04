from fastapi import FastAPI

app = FastAPI(
  title="Code TLDR",
  description="Code TLDR",
  version="0.1.0",
)

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/health")
async def health_check():
  return {"status": "healthy"}

