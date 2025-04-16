from typing import Annotated
from pydantic import BaseModel, Field
from app.core.logging import logger


class KeyResult(BaseModel):
    key: Annotated[str, Field(description="Tonic note (C, G#, etc.)")]
    mode: Annotated[str, Field(pattern="^(major|minor)$")]
    confidence: Annotated[float, Field(ge=0.0, le=1.0)]
    citation_ids: list[int] = []


async def predict_key(chords: list[str]) -> KeyResult:
    """
    Placeholder RAG agent.
    Next milestone: integrate LlamaIndex FunctionAgent.
    """
    logger.info("rag.predict_key.stub", chords=chords[:10])
    return KeyResult(key="C", mode="major", confidence=0.5)
