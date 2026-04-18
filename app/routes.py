from fastapi import APIRouter, HTTPException, Query
from app.ingestion import fetch_and_store_news
from app.processing import process_and_store
from app.db import processed_collection

router = APIRouter()

@router.post("/ingest")
def ingest_data():
    try:
        result = fetch_and_store_news()
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/process")
def process_data():
    try:
        result = process_and_store()
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/trends")
def get_trends(days: int = 7):
    try:
        data = list(processed_collection.find({}, {"_id": 0, "keywords": 1}))
        from collections import Counter
        all_keywords = []
        for x in data:
            all_keywords.extend(x.get("keywords", []))
        
        freq = Counter(all_keywords)
        top_keywords = [word for word, _ in freq.most_common(10)]
        return {"trends": top_keywords}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search")
def search(q: str = Query(None)):
    if not q:
        return {"error": "Please provide a search query"}

    results = list(processed_collection.find({
        "title": {"$regex": q, "$options": "i"}
    }))

    for r in results:
        r["_id"] = str(r["_id"])

    return {
        "query": q,
        "count": len(results),
        "results": results
    }

@router.get("/analytics/summary")
def get_analytics_summary():
    try:
        total = processed_collection.count_documents({})
        positive = processed_collection.count_documents({"sentiment": "positive"})
        negative = processed_collection.count_documents({"sentiment": "negative"})
        neutral = processed_collection.count_documents({"sentiment": "neutral"})
        
        data = list(processed_collection.find({}, {"_id": 0, "keywords": 1}))
        from collections import Counter
        all_keywords = []
        for x in data:
            all_keywords.extend(x.get("keywords", []))
        top_keywords = [word for word, _ in Counter(all_keywords).most_common(5)]
        
        return {
            "total_articles": total,
            "sentiment_counts": {
                "positive": positive,
                "negative": negative,
                "neutral": neutral
            },
            "top_trending_keywords": top_keywords
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))