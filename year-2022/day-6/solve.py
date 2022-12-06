#! /usr/bin/env python3

import itertools as it
import more_itertools as mit
import functools as ft
import regex as re
import numpy as np
import urllib3 as ul
import dateutil.parser as dp

from aocd import get_data, submit  # type: ignore

from share import *


PLACEHOLDER: object = object()


data: str = clean(get_data(year=2022, day=6))
sample_data: str = clean(
    """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""
)


def A(input: str) -> int:
    for index, window in enumerate(mit.windowed(by_chars(input), 4), 4):
        if len(set(window)) == 4:
            return index


def B(input: str) -> int:
    for index, window in enumerate(mit.windowed(by_chars(input), 14), 14):
        if len(set(window)) == 14:
            return index


assert A(sample_data) == 7, A(sample_data)
submit(A(data), part="a", day=6, year=2022)

assert B(sample_data) == 19, B(sample_data)
submit(B(data), part="b", day=6, year=2022)
