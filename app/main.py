from dotenv import load_dotenv
from pathlib import Path
import os

# Force load .env from ROOT folder
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

print("Loaded MONGO:", os.getenv("mongodb+srv://najamrizviofficial_db_user:vum08exgHPC0Vs42@cluster0.f9a6nyl.mongodb.net/trend-analytics"))  # debug

from fastapi import FastAPI
from app.routes import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running 🚀"}

app.include_router(router)