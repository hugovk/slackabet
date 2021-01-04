#!/usr/bin/env python3
"""
CLI for slackabet
"""
import argparse

import slackabet

try:
    import pyperclip
except ImportError:
    pyperclip = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="Text to convert to emoji")
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {slackabet.__version__}"
    )
    parser.add_argument("-w", "--white", action="store_true", help="White alphabet")
    parser.add_argument("-y", "--yellow", action="store_true", help="Yellow alphabet")
    parser.add_argument(
        "-r", "--random", action="store_true", help="Randomly coloured letters"
    )
    parser.add_argument(
        "--no-copy", action="store_true", help="Do not copy to clipboard"
    )
    args = parser.parse_args()

    colour = "white"
    if args.white:
        colour = "white"
    elif args.yellow:
        colour = "yellow"
    elif args.random:
        colour = "random"

    out = slackabet.slackabet(args.text, colour)
    print(out)
    if pyperclip and not args.no_copy:
        pyperclip.copy(out)
        print("Copied!")


if __name__ == "__main__":
    main()
