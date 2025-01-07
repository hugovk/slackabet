from __future__ import annotations

import random

from slackabet import _version

__version__ = _version.__version__

__all__ = ["__version__"]

COLOURS = ["white", "yellow"]


def slackabet(text: str, colour: str = "white") -> str:
    """Convert your text into alphabet emoji"""

    if colour == "words":
        words = text.split()
        converted = []
        for i, word in enumerate(words):
            colour = "white" if i % 2 == 0 else "yellow"

            converted.append(slackabet(word, colour))
        return " ".join(converted)

    new = ""
    prefix = f"alphabet-{colour}"
    for c in text:
        if colour == "random":
            prefix = f"alphabet-{random.choice(COLOURS)}"

        if c.isalpha():
            new += f":{prefix}-{c}:"
        elif c == "@":
            new += f":{prefix}-at:"
        elif c == "!":
            new += f":{prefix}-exclamation:"
        elif c == "#":
            new += f":{prefix}-hash:"
        elif c == "?":
            new += f":{prefix}-question:"
        else:
            new += c

    return new
