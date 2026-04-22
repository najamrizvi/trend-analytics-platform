from pymongo import MongoClient

# 🔴 Hardcode URI (temporary but guaranteed to work)
MONGO_URI = "MONGO_URI"

client = MongoClient(MONGO_URI)

db = client["trend_db"]

raw_collection = db["raw_data"]
processed_collection = db["processed_data"]