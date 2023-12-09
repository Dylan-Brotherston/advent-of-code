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


puzzle_data: str = clean(get_data(year=2023, day=9))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""), 114),
    ],
    "B": [
        (clean("""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""), 2),
    ],
}


def A(input: str) -> int:
    total = 0

    for line in input.splitlines():
        values = [int(x) for x in line.split()]
        seq: list[list[int]] = []
        seq.append(values)

        while not all(map(lambda x: x == 0, seq[-1])):
            next_seq = []
            for v1, v2 in pairwise(seq[-1]):
                next_seq.append(v2 - v1)
            seq.append(next_seq)

        seq[-1].append(0)
        while len(seq) > 1:
            s = seq.pop()[-1]
            last = seq[-1][-1]
            seq[-1].append(s + last)

        total += seq[0][-1]

    return total


def B(input: str) -> int:
    total = 0

    for line in input.splitlines():
        values = [int(x) for x in line.split()]
        seq: list[list[int]] = []
        seq.append(values)

        while not all(map(lambda x: x == 0, seq[-1])):
            next_seq = []
            for v1, v2 in pairwise(seq[-1]):
                next_seq.append(v2 - v1)
            seq.append(next_seq)

        seq[-1].insert(0, 0)
        while len(seq) > 1:
            s = seq.pop()[0]
            last = seq[-1][0]
            seq[-1].insert(0, last - s)

        total += seq[0][0]

    return total


for i, (data, solution) in enumerate(sample_data["A"], 1):
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for A, {recived=} == {solution=}")
submit((answer := A(puzzle_data)), part="a", day=9, year=2023)
print(f"submitted {answer=} for part A")

for i, (data, solution) in enumerate(sample_data["B"], 1):
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for B, {recived=} == {solution=}")
submit((answer := B(puzzle_data)), part="b", day=9, year=2023)
print(f"submitted {answer=} for part B")
