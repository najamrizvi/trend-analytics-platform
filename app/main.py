from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Trend Analytics Platform")

app.include_router(router)

@app.get("/")
def home():
    return {"status": "running", "message": "Trend Analytics API running 🚀"}