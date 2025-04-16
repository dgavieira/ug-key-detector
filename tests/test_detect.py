import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_post_detect(monkeypatch):
    # 1) monkey‑patch scraper to avoid real HTTP
    async def _fake_fetch(url: str) -> str:
        return '<span class="chord">C</span> text <span class="chord">F</span> <span class="chord">G</span>'
    monkeypatch.setattr("app.scraper.fetch.fetch_html", _fake_fetch)

    # 2) call API
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/detect", json={"url": "http://example.com"})
    assert resp.status_code == 200
    payload = resp.json()
    assert payload["key"] == "C"
