from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running on Railway 🚀"}

# SAFE IMPORT (prevents crash)
try:
    from app.routes import router
    app.include_router(router)
except Exception as e:
    print("Router import failed:", e)