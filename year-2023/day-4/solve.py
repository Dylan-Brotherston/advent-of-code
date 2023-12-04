#! /usr/bin/env python3

import sys
import os
import math
import statistics as stat
import functools as ft
import collections as coll
import itertools as it
import more_itertools as mit
import regex as re
import numpy as np
import sympy as syp
import scipy as scp
import urllib3 as ul
import requests as rq
import bs4 as bs
import dateutil.parser as dp

from textwrap import *
from string import *
from itertools import *
from operator import *
from more_itertools import *
from functools import partial, reduce, lru_cache, wraps, cmp_to_key
from collections import defaultdict, Counter, deque, namedtuple, OrderedDict
from dataclasses import dataclass
from aocd import get_data, submit  # type: ignore
from share import *


puzzle_data: str = clean(get_data(year=2023, day=4))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (
            clean(
                """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
            ),
            13,
        ),
    ],
    "B": [
        (
            clean(
                """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
            ),
            30,
        ),
    ],
}


def A(input: str) -> int:
    total = 0
    for line in input.splitlines():
        game, nums = line.split(":")
        winning, have = nums.split("|")
        winning = [int(x) for x in winning.split()]
        have = [int(x) for x in have.split()]
        points = None
        for card in have:
            if card in winning:
                points = points * 2 if points else 1
        total += points if points else 0

    return total


def B(input: str) -> int:
    multiplier = defaultdict(lambda: 1)
    total = 0
    for i, line in enumerate(input.splitlines(), 1):
        game, nums = line.split(":")
        winning, have = nums.split("|")
        winning = [int(x) for x in winning.split()]
        have = [int(x) for x in have.split()]

        count = 0
        for card in have:
            if card in winning:
                count += 1

        for count in range(1, count + 1):
            multiplier[count + i] += multiplier[i]

        total += multiplier[i]

    return total


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"{recived} != {solution}"
submit(A(puzzle_data), part="a", day=4, year=2023)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"{recived} != {solution}"
submit(B(puzzle_data), part="b", day=4, year=2023)
