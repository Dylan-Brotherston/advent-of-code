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


data: str = clean(get_data(year=2022, day=1))
sample_data: str = clean(
    """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
)


def sum_groups(groups: list[str]) -> list[int]:
    return lmap(lambda x: sum(to_ints(by_lines(x))), groups)


def A(input: str) -> int:
    input: list[int] = sum_groups(by_paragraphs(input))
    return max(input)


def B(input: str) -> int:
    input: list[int] = sum_groups(by_paragraphs(input))
    input.sort()
    return sum(input[-3:])


assert A(sample_data) == 24000, A(sample_data)
submit(A(data), part="a", day=1, year=2022)

assert B(sample_data) == 45000, B(sample_data)
submit(B(data), part="b", day=1, year=2022)
