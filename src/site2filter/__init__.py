# SPDX-License-Identifier: MIT
# Copyright (c) 2024 Mordarski Networks

"""site2filter is a Python program that turns a list of websites into a filter for uBlock Origin."""
from site2filter import parse_arguments


def site2filter():
    """site2filter."""
    parse_arguments.main()
