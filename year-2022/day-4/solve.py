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


data: str = clean(get_data(year=2022, day=4))
sample_data: str = clean(
    """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
)


def A(input: str) -> int:
    total = 0

    for line in by_lines(input):
        range1_start, range1_end, range2_start, range2_end = to_ints(
            nested_split(line, ",", "-")
        )
        range1, range2 = lirange(range1_start, range1_end), lirange(
            range2_start, range2_end
        )

        if len(set(range1) & set(range2)) == min(len(range1), len(range2)):
            total += 1

    return total


def B(input: str) -> int:
    total = 0

    for line in by_lines(input):
        range1_start, range1_end, range2_start, range2_end = to_ints(
            nested_split(line, ",", "-")
        )
        range1, range2 = lirange(range1_start, range1_end), lirange(
            range2_start, range2_end
        )

        if len(set(range1) & set(range2)) > 0:
            total += 1

    return total


assert A(sample_data) == 2, A(sample_data)
submit(A(data), part="a", day=4, year=2022)

assert B(sample_data) == 4, B(sample_data)
submit(B(data), part="b", day=4, year=2022)
