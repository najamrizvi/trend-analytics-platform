from fastapi import FastAPI
from app.routes import router

print("🚀 APP STARTED SUCCESSFULLY")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

app.include_router(router)