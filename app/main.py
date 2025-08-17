from fastapi import FastAPI
from app.routers import items

app = FastAPI()

app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/health")
def health():
    return {"status": "ok"}