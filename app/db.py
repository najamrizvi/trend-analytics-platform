import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI not set in environment variables")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client["trend_analytics"]

raw_collection = db["raw_data"]
processed_collection = db["processed_data"]

try:
    client.admin.command("ping")
    print("MongoDB Connected Successfully ✅")
except Exception as e:
    print("MongoDB Connection Failed ❌", e)