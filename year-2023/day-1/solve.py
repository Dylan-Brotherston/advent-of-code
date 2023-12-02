#! /usr/bin/env python3

import sys, os, math, statistics as stat
import itertools as it
import functools as ft
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
from functools import partial, reduce, lru_cache, wraps, cmp_to_key
from collections import defaultdict, Counter, deque, namedtuple, OrderedDict
from dataclasses import dataclass
from aocd import get_data, submit  # type: ignore
from share import *


puzzle_data: str = clean(get_data(year=2023, day=1))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (
            clean(
                """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
            ),
            142,
        ),
    ],
    "B": [
        (
            clean(
                """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
            ),
            281,
        ),
    ],
}


def A(input: str) -> int:
    n = []
    for line in input.splitlines():
        numbers = re.findall(r"\d", line)
        n.append(int(numbers[0] + numbers[-1]))

    return sum(n)


def B(input: str) -> int:
    n = []
    for line in input.splitlines():
        line = line\
            .replace("one", "on1e")\
            .replace("two", "tw2o")\
            .replace("three", "thre3e")\
            .replace("four", "fou4r")\
            .replace("five", "fiv5e")\
            .replace("six", "si6x")\
            .replace("seven", "seve7n")\
            .replace("eight", "eigh8t")\
            .replace("nine", "nin9e")
        numbers = re.findall(r"\d", line)
        n.append(int(numbers[0] + numbers[-1]))

    return sum(n)


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=1, year=2023)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=1, year=2023)
