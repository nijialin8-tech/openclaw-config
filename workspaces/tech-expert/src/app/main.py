from fastapi import FastAPI
from src.api.v1 import router as v1_router

app = FastAPI(title="Modern FastAPI Project", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello from Architect Lobster!"}

app.include_router(v1_router, prefix="/api/v1")
