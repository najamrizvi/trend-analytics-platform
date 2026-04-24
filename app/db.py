from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")

client = None
db = None
raw_collection = None
processed_collection = None

try:
    if MONGO_URI:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        
        # Force connection test
        client.server_info()
        
        db = client["trend_db"]
        raw_collection = db["raw_data"]
        processed_collection = db["processed_data"]
        
        print("✅ MongoDB connected successfully")

    else:
        print("⚠️ WARNING: MONGO_URI is not set")

except Exception as e:
    print("❌ MongoDB connection failed:", str(e))