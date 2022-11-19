from __future__ import annotations

import random

try:
    # Python 3.8+
    import importlib.metadata as importlib_metadata
except ImportError:
    # Python 3.7 and lower
    import importlib_metadata  # type: ignore

__version__: str = importlib_metadata.version(__name__)


COLOURS = ["white", "yellow"]


def slackabet(text: str, colour: str = "white") -> str:
    """Convert your text into alphabet emoji"""

    if colour == "words":
        words = text.split()
        converted = []
        for i, word in enumerate(words):
            if i % 2 == 0:
                colour = "white"
            else:
                colour = "yellow"
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
