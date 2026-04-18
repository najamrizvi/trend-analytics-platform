from app.db import raw_collection, processed_collection
from collections import Counter
import re

def extract_keywords(text):
    if not text:
        return []

    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    common_words = {"this", "that", "with", "from", "have", "will", "said", "they", "their", "them", "what", "when", "where", "which", "there", "about", "would", "could", "should", "some", "more"}
    
    filtered = [w for w in words if w not in common_words]
    freq = Counter(filtered)
    
    return [word for word, _ in freq.most_common(5)]

def get_sentiment(text):
    if not text:
        return "neutral"

    text = text.lower()
    positive_words = {"good", "great", "growth", "profit", "success", "positive", "rise", "boom", "high", "win"}
    negative_words = {"bad", "loss", "decline", "crisis", "fall", "negative", "war", "fail", "low", "crash"}

    words = set(re.findall(r'\b[a-z]{3,}\b', text))
    
    pos_score = len(words.intersection(positive_words))
    neg_score = len(words.intersection(negative_words))

    if pos_score > neg_score:
        return "positive"
    elif neg_score > pos_score:
        return "negative"
    else:
        return "neutral"

def calculate_trend_score(keywords):
    return len(keywords) * 2

def process_and_store():
    print("1. Processing started")
    
    try:
        articles_cursor = raw_collection.find()
        articles = list(articles_cursor)
    except Exception as e:
        return {"error": f"Database fetch failed: {str(e)}"}

    print("2. Articles fetched:", len(articles))

    if not articles:
        return {"message": "No raw data found to process.", "count": 0}

    processed_data = []

    for article in articles:
        text = (article.get("title") or "") + " " + (article.get("content") or "")
        keywords = extract_keywords(text)
        sentiment = get_sentiment(text)
        trend_score = calculate_trend_score(keywords)

        processed_data.append({
            "title": article.get("title"),
            "keywords": keywords,
            "sentiment": sentiment,
            "trend_score": trend_score
        })

    print("3. Loop finished")

    if processed_data:
        try:
            processed_collection.delete_many({}) 
            processed_collection.insert_many(processed_data)
            print("4. Insert done")
        except Exception as e:
            return {"error": f"Database insertion failed: {str(e)}"}
    else:
        print("No data to insert")

    return {
        "message": "Processing completed",
        "count": len(processed_data)
    }