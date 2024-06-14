# SPDX-License-Identifier: MIT
# Copyright (c) 2024 Mordarski Networks

"""site2filter is a Python program that turns a list of websites into a filter for uBlock Origin."""
import argparse


def main():
    """This is a function to parse arguments."""
    parser = argparse.ArgumentParser(
        prog="site2filter",
        description=__doc__,
    )
    parser.add_argument("-f", "--filter", nargs=1, help="Choose a filter.")
    parser.add_argument("-l", "--list", help="List all available filters.")
    parser.add_argument(
        "-w",
        "--word",
        nargs=1,
        help="Give a list of websites or words seperated by a space to be blocked.",
    )
    args = parser.parse_args()

    if args.filter:
        pass
    if args.list:
        pass
    if args.word:
        pass
