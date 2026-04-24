from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Trend Analytics API",
    description="AI-powered market intelligence platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

app.include_router(router)