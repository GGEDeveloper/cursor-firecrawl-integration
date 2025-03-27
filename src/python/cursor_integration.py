from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .scraper import Scraper, ScraperConfig

app = FastAPI()
scraper = None

class ScrapingRequest(BaseModel):
    url: str
    formats: Optional[List[str]] = None
    params: Optional[Dict] = None

class BatchScrapingRequest(BaseModel):
    urls: List[str]
    formats: Optional[List[str]] = None
    params: Optional[Dict] = None

class SearchRequest(BaseModel):
    query: str
    max_results: Optional[int] = 5

@app.on_event("startup")
async def startup_event():
    global scraper
    scraper = Scraper()

@app.post("/scrape")
async def scrape_endpoint(request: ScrapingRequest):
    """
    Endpoint for scraping a single URL
    """
    if not scraper:
        raise HTTPException(status_code=500, detail="Scraper not initialized")
    
    params = request.params or {}
    if request.formats:
        params["formats"] = request.formats
    
    result = await scraper.scrape_url(request.url, params)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result

@app.post("/batch-scrape")
async def batch_scrape_endpoint(request: BatchScrapingRequest):
    """
    Endpoint for batch scraping multiple URLs
    """
    if not scraper:
        raise HTTPException(status_code=500, detail="Scraper not initialized")
    
    params = request.params or {}
    if request.formats:
        params["formats"] = request.formats
    
    result = await scraper.batch_scrape(request.urls, params)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result

@app.post("/search")
async def search_endpoint(request: SearchRequest):
    """
    Endpoint for searching and scraping content
    """
    if not scraper:
        raise HTTPException(status_code=500, detail="Scraper not initialized")
    
    result = await scraper.search_and_scrape(request.query, request.max_results)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result

@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy", "scraper_initialized": scraper is not None}