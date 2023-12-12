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


puzzle_data: str = clean(get_data(year=2023, day=11))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""), 374),
    ],
    "B": [
        (clean("""
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""), 82000210),
    ],
}


@dataclass
class Point(object):
    row: int
    col: int

    def __hash__(self) -> int:
        return hash((self.row, self.col))


def A(input: str) -> int:
    galaxies: set[Point] = set()
    non_empty_rows: set[int] = set()
    non_empty_cols: set[int] = set()
    for row, line in enumerate(input.splitlines()):
        for col, char in enumerate(line):
            if char == "#":
                galaxies.add(Point(row, col))
                non_empty_rows.add(row)
                non_empty_cols.add(col)

    empty_rows = set(range(0, max(non_empty_rows))) - non_empty_rows
    for galaxie in galaxies:
        gr = galaxie.row
        for row in empty_rows:
            if galaxie.row > row:
                gr += 1
        galaxie.row = gr

    empty_cols = set(range(0, max(non_empty_cols))) - non_empty_cols
    for galaxie in galaxies:
        gc = galaxie.col
        for col in empty_cols:
            if galaxie.col > col:
                gc += 1
        galaxie.col = gc

    total = 0
    for galaxyA, galaxyB in combinations(galaxies, 2):
        total += abs(galaxyA.row - galaxyB.row) + abs(galaxyA.col - galaxyB.col)

    return total


def B(input: str) -> int:
    galaxies: set[Point] = set()
    non_empty_rows: set[int] = set()
    non_empty_cols: set[int] = set()
    for row, line in enumerate(input.splitlines()):
        for col, char in enumerate(line):
            if char == "#":
                galaxies.add(Point(row, col))
                non_empty_rows.add(row)
                non_empty_cols.add(col)

    empty_rows = set(range(0, max(non_empty_rows))) - non_empty_rows
    for galaxie in galaxies:
        gr = galaxie.row
        for row in empty_rows:
            if galaxie.row > row:
                gr += 999_999
        galaxie.row = gr

    empty_cols = set(range(0, max(non_empty_cols))) - non_empty_cols
    for galaxie in galaxies:
        gc = galaxie.col
        for col in empty_cols:
            if galaxie.col > col:
                gc += 999_999
        galaxie.col = gc

    total = 0
    for galaxyA, galaxyB in combinations(galaxies, 2):
        total += abs(galaxyA.row - galaxyB.row) + abs(galaxyA.col - galaxyB.col)

    return total


for i, (data, solution) in enumerate(sample_data["A"], 1):
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for A, {recived=} == {solution=}")
submit((answer := A(puzzle_data)), part="a", day=11, year=2023)
print(f"submitted {answer=} for part A")

for i, (data, solution) in enumerate(sample_data["B"], 1):
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for B, {recived=} == {solution=}")
submit((answer := B(puzzle_data)), part="b", day=11, year=2023)
print(f"submitted {answer=} for part B")
