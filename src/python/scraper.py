from typing import Dict, List, Optional, Union
from firecrawl.firecrawl import FirecrawlApp
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

class ScraperConfig(BaseModel):
    api_key: str = os.getenv("FIRECRAWL_API_KEY", "")
    formats: List[str] = ["markdown", "html"]
    max_pages: int = 10
    timeout: int = 30

class Scraper:
    def __init__(self, config: Optional[ScraperConfig] = None):
        self.config = config or ScraperConfig()
        self.app = FirecrawlApp(api_key=self.config.api_key)

    async def scrape_url(self, url: str, params: Optional[Dict] = None) -> Dict:
        """
        Scrape a single URL and return the content in specified formats
        """
        default_params = {
            "formats": self.config.formats
        }
        scrape_params = {**default_params, **(params or {})}
        
        try:
            result = await self.app.scrape_url(url, scrape_params)
            return {
                "success": True,
                "data": result.data if hasattr(result, "data") else result,
                "url": url
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "url": url
            }

    async def batch_scrape(self, urls: List[str], params: Optional[Dict] = None) -> Dict:
        """
        Scrape multiple URLs in batch
        """
        default_params = {
            "formats": self.config.formats
        }
        scrape_params = {**default_params, **(params or {})}
        
        try:
            result = await self.app.batch_scrape(urls, scrape_params)
            return {
                "success": True,
                "data": result,
                "urls": urls
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "urls": urls
            }

    async def extract_structured_data(self, url: str, schema: BaseModel) -> Dict:
        """
        Extract structured data from a URL using a Pydantic schema
        """
        try:
            result = await self.app.scrape_url(url, {
                "formats": ["json"],
                "jsonOptions": {
                    "schema": schema.model_json_schema()
                }
            })
            return {
                "success": True,
                "data": result.data["json"] if "json" in result.data else result.data,
                "url": url
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "url": url
            }

    async def search_and_scrape(self, query: str, max_results: int = 5) -> Dict:
        """
        Search for content and scrape the results
        """
        try:
            search_result = await self.app.search(query, {
                "scrapeOptions": {
                    "formats": self.config.formats
                },
                "limit": max_results
            })
            return {
                "success": True,
                "data": search_result,
                "query": query
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "query": query
            }