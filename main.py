# main.py
from fastapi import FastAPI, Header, HTTPException
from duckduckgo_search import DDGS
import os

app = FastAPI()

# Ye aapki secret API key hai (Render ke dashboard se set hogi ya default ye chalegi)
API_SECRET_KEY = os.getenv("TOOL_API_KEY", "my_custom_secret_key_786")

@app.get("/")
def home():
    return {"status": "Search API is running online!"}

@app.get("/images")
def search_images(query: str, count: int = 5, x_api_key: str = Header(None)):
    if x_api_key != API_SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    with DDGS() as ddgs:
        # DDGS internet se direct images fetch karega
        results = list(ddgs.images(query, max_results=count))
    return {"query": query, "type": "images", "results": results}

@app.get("/videos")
def search_videos(query: str, count: int = 5, x_api_key: str = Header(None)):
    if x_api_key != API_SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    with DDGS() as ddgs:
        # DDGS internet se direct videos fetch karega
        results = list(ddgs.videos(query, max_results=count))
    return {"query": query, "type": "videos", "results": results}