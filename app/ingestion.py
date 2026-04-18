import os
import requests
from dotenv import load_dotenv
from app.db import raw_collection

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

def fetch_and_store_news():
    if not API_KEY:
        raise ValueError("NEWS_API_KEY not set in environment variables.")

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch news: {str(e)}"}

    articles = response.json().get("articles", [])
    if not articles:
        return {"message": "No articles fetched."}

    cleaned_data = []

    for article in articles:
        cleaned_data.append({
            "title": article.get("title"),
            "content": article.get("description"),
            "source": article.get("source", {}).get("name"),
            "published_at": article.get("publishedAt"),
            "category": "general"
        })

    if cleaned_data:
        try:
            raw_collection.insert_many(cleaned_data)
        except Exception as e:
            return {"error": f"Database insertion failed: {str(e)}"}

    return {"message": "Data stored successfully", "count": len(cleaned_data)}