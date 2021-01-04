import random

import pkg_resources

__version__: str = pkg_resources.get_distribution(__name__).version


COLOURS = ["white", "yellow"]


def slackabet(text: str, colour: str = "white") -> str:
    """Convert your text into alphabet emoji"""
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
