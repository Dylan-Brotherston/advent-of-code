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


data: str = clean(get_data(year=2022, day=3))
sample_data: str = clean(
    """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
)


def A(input: str) -> int:
    total = 0

    for line in by_lines(input):

        length = len(line)
        first_half, second_half = line[: length // 2], line[length // 2 :]
        first_half, second_half = set(first_half), set(second_half)
        intersection = first_half & second_half
        assert len(intersection) == 1
        intersection = intersection.pop()

        if intersection.islower():
            total += ord(intersection) - ord("a") + 1
        if intersection.isupper():
            total += ord(intersection) - ord("A") + 27

    return total


def B(input: str) -> int:
    total = 0

    for line_1, line_2, line_3 in mit.chunked(by_lines(input), 3):

        line_1, line_2, line_3 = set(line_1), set(line_2), set(line_3)
        intersection = line_1 & line_2 & line_3
        assert len(intersection) == 1
        intersection = intersection.pop()

        if intersection.islower():
            total += ord(intersection) - ord("a") + 1
        if intersection.isupper():
            total += ord(intersection) - ord("A") + 27

    return total


assert A(sample_data) == 157, A(sample_data)
submit(A(data), part="a", day=3, year=2022)

assert B(sample_data) == 70, B(sample_data)
submit(B(data), part="b", day=3, year=2022)
