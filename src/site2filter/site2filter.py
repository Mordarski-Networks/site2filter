# SPDX-License-Identifier: MIT
# Copyright (c) 2024 Mordarski Networks

"""site2filter is a Python program that turns a list of websites into a filter for uBlock Origin."""
import argparse
import platform
import subprocess


def main():
    """This is a function to parse arguments."""
    parser = argparse.ArgumentParser(
        prog="site2filter",
        description=__doc__,
    )
    args = parser.parse_args()
    parser.add_argument("-f", "--filter", nargs=1, help="Choose a filter.")
    parser.add_argument("-l", "--list", help="List all available filters.")
    parser.add_argument(
        "-w",
        "--word",
        nargs=1,
        help="Give a list of websites or words seperated by a space to be blocked.",
    )

    if args.filter:
        pass
    if args.list:
        pass
    if args.word:
        pass


def read_filter():
    """Read a filter from a file."""


def generate_filter():
    """Generate a filter."""


def copy(string):
    """Copy a given argument to the clipboard.

    The argument should be a string.
    """
    os_dictionary = {"Windows": "clip", "Linux": "xclip -sel clip", "Darwin": "pbcopy"}

    for keys, vaules in os_dictionary.items():
        if platform.system() == keys:
            subprocess.run(vaules, check=False, Shell=False, input=string.encode())


if __name__ == "__main__":
    main()
