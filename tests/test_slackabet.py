from hypothesis_auto import auto_pytest_magic

import slackabet


def test_something():
    # Arrange

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


def test_something_else():
    # Arrange

    # Act
    text = slackabet.slackabet("123ABCabc@!#?", colour="yellow")

    # Assert
    assert (
        text == "123"
        ":alphabet-yellow-A::alphabet-yellow-B::alphabet-yellow-C:"
        ":alphabet-yellow-a::alphabet-yellow-b::alphabet-yellow-c:"
        ":alphabet-yellow-at:"
        ":alphabet-yellow-exclamation:"
        ":alphabet-yellow-hash:"
        ":alphabet-yellow-question:"
    )


auto_pytest_magic(slackabet.slackabet)
