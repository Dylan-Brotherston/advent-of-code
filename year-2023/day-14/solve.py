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
from copy import deepcopy

from aocd import get_data, submit  # type: ignore

from share import *


puzzle_data: str = clean(get_data(year=2023, day=14))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""), 136),
    ],
    "B": [
        (clean("""
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""), 64),
    ],
}


def A(input: str) -> int:
    grid: list[list[str]] = [[char for char in line] for line in input.splitlines()]

    for i, line in enumerate(grid):
        if i == 0:
            continue
        for j, char in enumerate(line):
            if grid[i][j] == "O" and grid[i - 1][j] == ".":
                di = -1
                while i + di >= 0 and grid[i + di][j] == ".":
                    di -= 1
                di += 1
                grid[i + di][j] = "O"
                grid[i][j] = "."

    total = 0
    for i, line in enumerate(reversed(grid), 1):
        for j, char in enumerate(line):
            if char == "O":
                total += i

    return total


def B(input: str) -> int:
    grid: list[list[str]] = [[char for char in line] for line in input.splitlines()]

    history: OrderedDict[str, int] = OrderedDict()
    history[tuple(tuple(line) for line in grid)] = 0

    for count in range(1, 1_000_000_000 + 1):

        # move north
        for i, line in enumerate(grid):
            if i == 0:
                continue
            for j, char in enumerate(line):
                if grid[i][j] == "O" and grid[i - 1][j] == ".":
                    di = -1
                    while i + di >= 0 and grid[i + di][j] == ".":
                        di -= 1
                    di += 1
                    grid[i + di][j] = "O"
                    grid[i][j] = "."

        # move west
        for i, line in enumerate(grid):
            for j, char in enumerate(line):
                if j == 0:
                    continue
                if grid[i][j] == "O" and grid[i][j - 1] == ".":
                    dj = -1
                    while j + dj >= 0 and grid[i][j + dj] == ".":
                        dj -= 1
                    dj += 1
                    grid[i][j + dj] = "O"
                    grid[i][j] = "."

        # move south
        for i, line in reversed(list(enumerate(reversed(grid)))):
            if i == len(grid) - 1:
                continue
            for j, char in enumerate(line):
                if grid[i][j] == "O" and grid[i + 1][j] == ".":
                    di = 1
                    while i + di < len(grid) and grid[i + di][j] == ".":
                        di += 1
                    di -= 1
                    grid[i + di][j] = "O"
                    grid[i][j] = "."

        # move east
        for i, line in enumerate(reversed(grid)):
            for j, char in reversed(list(enumerate(line))):
                if j == len(line) - 1:
                    continue
                if grid[i][j] == "O" and grid[i][j + 1] == ".":
                    dj = 1
                    while j + dj < len(line) and grid[i][j + dj] == ".":
                        dj += 1
                    dj -= 1
                    grid[i][j + dj] = "O"
                    grid[i][j] = "."

        grid_tuple = tuple(tuple(line) for line in grid)
        if grid_tuple in history.keys():
            cycle_length = count - history[grid_tuple]
            index = history[grid_tuple] + (1_000_000_000 - history[grid_tuple]) % cycle_length
            grid = list(history.keys())[index]
            break
        else:
            history[grid_tuple] = count

    total = 0
    for i, line in enumerate(reversed(grid), 1):
        for j, char in enumerate(line):
            if char == "O":
                total += i

    return total


for i, (data, solution) in enumerate(sample_data["A"], 1):
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for A, {recived=} == {solution=}")
submit((answer := A(puzzle_data)), part="a", day=14, year=2023)
print(f"submitted {answer=} for part A")

for i, (data, solution) in enumerate(sample_data["B"], 1):
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for B, {recived=} == {solution=}")
submit((answer := B(puzzle_data)), part="b", day=14, year=2023)
print(f"submitted {answer=} for part B")
