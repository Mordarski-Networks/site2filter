# SPDX-License-Identifier: MIT
# Copyright (c) 2024 Mordarski Networks

"""This module allows you to copy a given argument to the clipboard."""
import platform
import subprocess


def copy(string):
    """Copy a given argument to the clipboard.

    The argument should be a string.
    """
    os_dictionary = {"Windows": "clip", "Linux": "xclip -sel clip", "Darwin": "pbcopy"}

    for keys, vaules in os_dictionary.items():
        if platform.system() == keys:
            subprocess.run(vaules, check=False, Shell=False, input=string.encode())
            return True

    return False
