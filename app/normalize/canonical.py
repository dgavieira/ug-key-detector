# app/normalize/canonical.py

import re
from app.core.logging import logger

# Matches root note (A–G plus optional #/b) and optional minor indicator
_PATTERN = re.compile(r"^([A-G][b#]?)(?:m|min)?")

def canonicalize(chord: str) -> str | None:
    """
    Return a canonical triad symbol (e.g. "C", "Dm", "F#") or None if unrecognized.
    Drops all extensions (7ths, sus, add, etc.) and only keeps major or minor.
    """
    chord = chord.strip()
    match = _PATTERN.match(chord)
    if not match:
        logger.warning("canonical.failed", chord=chord)
        return None

    root = match.group(1)
    quality_suffix = "m" if chord[len(root):].startswith(("m", "min")) else ""
    canon = f"{root}{quality_suffix}"
    logger.debug("canonical", inp=chord, out=canon)
    return canon
