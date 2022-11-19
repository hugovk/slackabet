from __future__ import annotations

import pytest
from hypothesis_auto import auto_pytest_magic  # type: ignore[import]

import slackabet


def test_slackabet_default() -> None:
    # Act
    text = slackabet.slackabet("123ABCabc@!#?")

    # Assert
    assert (
        text == "123"
        ":alphabet-white-A::alphabet-white-B::alphabet-white-C:"
        ":alphabet-white-a::alphabet-white-b::alphabet-white-c:"
        ":alphabet-white-at:"
        ":alphabet-white-exclamation:"
        ":alphabet-white-hash:"
        ":alphabet-white-question:"
    )


@pytest.mark.parametrize(
    ("test_colour", "expected"),
    [
        ("yellow", ":alphabet-yellow-A:"),
        ("white", ":alphabet-white-A:"),
    ],
)
def test_slackabet_colour(test_colour: str, expected: str) -> None:
    # Act
    text = slackabet.slackabet("A", colour=test_colour)

    # Assert
    assert text == expected


def test_slackabet_random() -> None:
    # Act
    text = slackabet.slackabet("A", colour="random")

    # Assert
    assert ":alphabet-" in text
    assert "-A:" in text


def test_slackabet_words() -> None:
    # Act
    text = slackabet.slackabet("hello there", colour="words")

    # Assert
    words = text.split()
    assert "alphabet-white-" in words[0]
    assert "alphabet-yellow-" in words[1]
    assert "alphabet-yellow-" not in words[0]
    assert "alphabet-white-" not in words[1]


auto_pytest_magic(slackabet.slackabet)
