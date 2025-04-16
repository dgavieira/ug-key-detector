# app/main.py

from fastapi import FastAPI, HTTPException
from app.schema import DetectRequest
from app.extract.chords import extract_chords
from app.normalize.canonical import canonicalize
from app.rag.agent import predict_key, KeyResult

app = FastAPI(title="UG Key Detector RAG", version="0.1.0")


@app.post("/detect", response_model=KeyResult)
async def detect(req: DetectRequest):
    # dynamic import so monkeypatching app.scraper.fetch.fetch_html works
    from app.scraper.fetch import fetch_html

    html = await fetch_html(str(req.url))
    raw_chords = extract_chords(html)
    if not raw_chords:
        raise HTTPException(status_code=422, detail="No chords found.")
    triads = [c for c in (canonicalize(ch) for ch in raw_chords) if c]
    if not triads:
        raise HTTPException(status_code=422, detail="No valid chords after normalization.")
    result = await predict_key(triads)
    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
