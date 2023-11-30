#! /usr/bin/env python3

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

from textwrap import dedent, indent
from aocd import get_data, submit  # type: ignore
from share import *


puzzle_data: str = clean(get_data(year=2015, day=6))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
    ],
    "B": [
    ],
}


def A(input: str) -> int:
    grid = defaultdict(lambda: False)

    for line in input.splitlines():
        if m := re.fullmatch(r"turn on (\d+),(\d+) through (\d+),(\d+)",  line):
            x1, y1, x2, y2 = map(int, m.groups())
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x, y] = True
        if m := re.fullmatch(r"turn off (\d+),(\d+) through (\d+),(\d+)", line):
            x1, y1, x2, y2 = map(int, m.groups())
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x, y] = False
        if m := re.fullmatch(r"toggle (\d+),(\d+) through (\d+),(\d+)",   line):
            x1, y1, x2, y2 = map(int, m.groups())
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x, y] = not grid[x, y]

    return sum(grid.values())


def B(input: str) -> int:
    grid = defaultdict(lambda: 0)

    for line in input.splitlines():
        if m := re.fullmatch(r"turn on (\d+),(\d+) through (\d+),(\d+)",  line):
            x1, y1, x2, y2 = map(int, m.groups())
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x, y] += 1
        if m := re.fullmatch(r"turn off (\d+),(\d+) through (\d+),(\d+)", line):
            x1, y1, x2, y2 = map(int, m.groups())
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x, y] -= 1
                    if grid[x, y] < 0:
                        grid[x, y] = 0
        if m := re.fullmatch(r"toggle (\d+),(\d+) through (\d+),(\d+)",   line):
            x1, y1, x2, y2 = map(int, m.groups())
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x, y] += 2

    return sum(grid.values())


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=6, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=6, year=2015)
