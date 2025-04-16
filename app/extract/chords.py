import re
from bs4 import BeautifulSoup
from typing import Iterator
from app.core.logging import logger

_CHORD_SPAN = re.compile(r"^[A-G][b#]?(m|min)?\d?(sus|add)?\d?(\/[A-G][b#]?)?$")
_BRACKET_RE = re.compile(r"\[([^\]]+)]")


def _is_chord(token: str) -> bool:
    return bool(_CHORD_SPAN.match(token.strip()))


def extract_chords(html: str) -> list[str]:
    """Return a list of raw chord symbols as they appear in the UG page."""
    soup = BeautifulSoup(html, "lxml")
    raw: list[str] = []

    # 1) <span class="chord">C</span>
    for span in soup.select("span.chord"):
        txt = span.get_text(strip=True)
        if _is_chord(txt):
            raw.append(txt)

    # 2) Plain‑text view sometimes embedded in <pre>
    for pre in soup.find_all("pre"):
        for token in _BRACKET_RE.findall(pre.get_text()):
            if _is_chord(token):
                raw.append(token)

    logger.info("extract.chords", count=len(raw))
    return raw
