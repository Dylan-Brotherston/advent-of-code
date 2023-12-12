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
from functools import partial, reduce, cache, cache as memoize, lru_cache, wraps, cmp_to_key
from collections import defaultdict, Counter, deque, namedtuple, OrderedDict
from dataclasses import dataclass
from pprint import pprint

from aocd import get_data, submit  # type: ignore

from share import *


puzzle_data: str = clean(get_data(year=2023, day=12))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""), 21),
    ],
    "B": [
        (clean("""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""), 525152),
    ],
}

def A(input: str) -> int:
    total = 0

    for line in input.splitlines():
        springs, count = line.split()
        count = lmap(int, count.split(","))
        Nmissing = Counter(springs)["?"]

        for replacement in product(".#", repeat=Nmissing):
            new_springs = springs.replace("?", "{}").format(*replacement)
            new_springs = lfilter(None, map(len, new_springs.split(".")))
            if new_springs == count:
                total += 1

    return total


def B(input: str) -> int:
    total = 0

    @memoize
    def valid(s: int, n: int, springs: str, count: tuple[int, ...]) -> int:
        if s >= len(springs):
            return n == len(count)

        ways = 0

        if springs[s] == "?" or springs[s] == ".":
            ways += valid(s + 1, n, springs, count)

        if n >= len(count):
            return ways


        if springs[s] == "?" or springs[s] == "#":
            end = s + count[n]
            if end <= len(springs):
                sl = springs[s:end]
                if "." not in sl and (end == len(springs) or springs[end] != "#"):
                    ways += valid(end + 1, n + 1, springs, count)

        return ways

    for line in input.splitlines():
        springs, count = line.split()
        springs = f"{springs}?{springs}?{springs}?{springs}?{springs}"
        count = f"{count},{count},{count},{count},{count}"
        count = lmap(int, count.split(","))

        total += valid(0, 0, springs, tuple(count))

    return total


for i, (data, solution) in enumerate(sample_data["A"], 1):
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for A, {recived=} == {solution=}")
submit((answer := A(puzzle_data)), part="a", day=12, year=2023)
print(f"submitted {answer=} for part A")

for i, (data, solution) in enumerate(sample_data["B"], 1):
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for B, {recived=} == {solution=}")
submit((answer := B(puzzle_data)), part="b", day=12, year=2023)
print(f"submitted {answer=} for part B")
