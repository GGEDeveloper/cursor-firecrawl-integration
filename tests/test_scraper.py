import pytest
from src.python.scraper import Scraper, ScraperConfig
from pydantic import BaseModel
from typing import List

class TestArticle(BaseModel):
    title: str
    content: str

@pytest.fixture
def scraper():
    config = ScraperConfig(api_key="test_key")
    return Scraper(config)

@pytest.mark.asyncio
async def test_scrape_url(scraper):
    result = await scraper.scrape_url("https://example.com")
    assert result["success"] is True
    assert "data" in result
    assert result["url"] == "https://example.com"

@pytest.mark.asyncio
async def test_batch_scrape(scraper):
    urls = ["https://example.com", "https://example.org"]
    result = await scraper.batch_scrape(urls)
    assert result["success"] is True
    assert "data" in result
    assert result["urls"] == urls

@pytest.mark.asyncio
async def test_extract_structured_data(scraper):
    class ArticleSchema(BaseModel):
        title: str
        content: str

    result = await scraper.extract_structured_data(
        "https://example.com",
        ArticleSchema
    )
    assert result["success"] is True
    assert "data" in result
    assert result["url"] == "https://example.com"

@pytest.mark.asyncio
async def test_search_and_scrape(scraper):
    result = await scraper.search_and_scrape("test query")
    assert result["success"] is True
    assert "data" in result
    assert result["query"] == "test query"