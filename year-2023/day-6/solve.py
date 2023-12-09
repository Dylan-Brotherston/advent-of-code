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
from pprint import pprint

from aocd import get_data, submit  # type: ignore

from share import *


puzzle_data: str = clean(get_data(year=2023, day=6))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
Time:      7  15   30
Distance:  9  40  200
"""), 288),
    ],
    "B": [
        (clean("""
Time:      7  15   30
Distance:  9  40  200
"""), 71503),
    ],
}


def A(input: str) -> int:
    time, distance = [lmap(int, line.split(":")[1].split()) for line in input.splitlines()]

    total = []
    for t, d in zip(time, distance):
        best = 0
        for T in range(t + 1):
            D = T * (t - T)
            if D > d:
                best += 1
        total.append(best)

    return prod(total)


def B(input: str) -> int:
    time, distance = [int(re.sub(r"\D", "", line)) for line in input.splitlines()]

    best = 0
    for T in range(time + 1):
        D = T * (time - T)
        if D > distance:
            best += 1
    return best


for i, (data, solution) in enumerate(sample_data["A"], 1):
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for A, {recived=} == {solution=}")
submit((answer := A(puzzle_data)), part="a", day=6, year=2023)
print(f"submitted {answer=} for part A")

for i, (data, solution) in enumerate(sample_data["B"], 1):
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for B, {recived=} == {solution=}")
submit((answer := B(puzzle_data)), part="b", day=6, year=2023)
print(f"submitted {answer=} for part B")
