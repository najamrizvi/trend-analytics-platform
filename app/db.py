from pymongo import MongoClient
import os

MONGO_URI = os.getenv("mongodb+srv://najamrizviofficial_db_user:vum08exgHPC0Vs42@cluster0.f9a6nyl.mongodb.net/trend-analytics")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

db = client["trend_db"]

raw_collection = db["raw_data"]
processed_collection = db["processed_data"]