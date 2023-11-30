#! /usr/bin/env python3

import sys, os
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


puzzle_data: str = clean(get_data(year=2015, day=18))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
    ],
    "B": [
    ],
}


def A(input: str) -> int:
    grid = [[c == "#" for c in line] for line in input.splitlines()]

    for _ in range(100):
        grid = [[
            (neighbors := sum(
                grid[y + dy][x + dx]
                for dy in [-1, 0, 1]
                for dx in [-1, 0, 1]
                if (dy, dx) != (0, 0)
                if 0 <= y + dy < len(grid)
                if 0 <= x + dx < len(grid[y + dy])
            )) == 3 or (
                grid[y][x] and neighbors == 2
            )
            for x in range(len(grid[y]))
        ] for y in range(len(grid))]

    return sum(sum(row) for row in grid)

def B(input: str) -> int:
    grid = [[c == "#" for c in line] for line in input.splitlines()]

    grid[0][0] = True
    grid[0][-1] = True
    grid[-1][0] = True
    grid[-1][-1] = True

    for _ in range(100):
        grid = [[
            (neighbors := sum(
                grid[y + dy][x + dx]
                for dy in [-1, 0, 1]
                for dx in [-1, 0, 1]
                if (dy, dx) != (0, 0)
                if 0 <= y + dy < len(grid)
                if 0 <= x + dx < len(grid[y + dy])
            )) == 3 or (
                grid[y][x] and neighbors == 2
            )
            for x in range(len(grid[y]))
        ] for y in range(len(grid))]

        grid[0][0] = True
        grid[0][-1] = True
        grid[-1][0] = True
        grid[-1][-1] = True

    return sum(sum(row) for row in grid)


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=18, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=18, year=2015)
