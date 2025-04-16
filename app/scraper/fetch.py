from httpx import AsyncClient, TimeoutException
from bs4 import BeautifulSoup
from app.core.config import get_settings
from app.core.logging import logger


async def fetch_html(url: str) -> str:
    """Download a UG page and return HTML (string)."""
    settings = get_settings()
    headers = {"User-Agent": settings.user_agent}
    try:
        async with AsyncClient(headers=headers, follow_redirects=True, timeout=settings.timeout_s) as client:
            r = await client.get(url)
            r.raise_for_status()
            logger.info("scraper.fetch_html.ok", url=url, bytes=len(r.text))
            return r.text
    except TimeoutException:
        logger.error("scraper.fetch_html.timeout", url=url)
        raise
