#!/usr/bin/env python3
"""
CLI for slackabet
"""
import argparse

import slackabet


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
    args = parser.parse_args()

    colour = "white"
    if args.white:
        colour = "white"
    elif args.yellow:
        colour = "yellow"
    elif args.random:
        colour = "random"

    print(slackabet.slackabet(args.text, colour))


if __name__ == "__main__":
    main()
