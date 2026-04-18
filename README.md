# Trend Analytics Platform

A production-ready FastAPI backend for fetching and analyzing trending news topics.

## Setup

1. Copy `.env` file and set your `MONGO_URI` and `NEWS_API_KEY`.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Endpoints

- `POST /ingest`: Fetches NewsAPI data and stores it in the `raw_data` collection safely.
- `POST /process`: Processes text to extract keywords and determine sentiment, storing in `processed_data`.
- `GET /trends?days=7`: Returns the top trending keywords.
- `GET /search?q=keyword`: Searches processed documentation by keyword or title.
- `GET /analytics/summary`: Returns simple analytics summary statistics.
