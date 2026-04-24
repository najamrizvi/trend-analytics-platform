from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")

client = None
db = None
raw_collection = None
processed_collection = None

if MONGO_URI:
    client = MongoClient(MONGO_URI)
    db = client["trend_db"]
    raw_collection = db["raw_data"]
    processed_collection = db["processed_data"]
else:
    print("WARNING: MONGO_URI is not set")