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


puzzle_data: str = clean(get_data(year=2023, day=13))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""), 405),
    ],
    "B": [
        (clean("""
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""), 400),
    ],
}


def A(input: str) -> int:
    total = 0

    for pattern in input.split("\n\n"):
        pattern = pattern.strip()
        grid = [list(line) for line in pattern.splitlines()]

        def fold(grid, axis, offset) -> bool:

            if axis == 1:
                new_grid = []
                for i in range(len(grid[0])):
                    new_grid.append([row[i] for row in grid])
                grid = new_grid

            if offset < math.ceil(len(grid[0]) // 2):
                new_grid = []
                for row in grid:
                    new_grid.append(row[::-1])
                grid = new_grid
                offset = len(grid[0]) - offset -2

            for i in range(len(grid)):
                right = grid[i][offset + 1:]
                left = (grid[i][:offset + 1])[-len(right):]
                if left != right[::-1]:
                    return False

            return True

        for axis in range(0, 2):
            limit = len(grid[0]) if axis == 0 else len(grid)
            for offset in range(limit - 1):
                if fold(grid, axis, offset):
                    if axis == 0:
                        total += offset + 1
                    else:
                        total += 100 * (offset + 1)
                    break
            else:
                continue
            break
        else:
            raise ValueError("no fold found")

    return total


def B(input: str) -> int:
    total = 0

    for pattern in input.split("\n\n"):
        pattern = pattern.strip()
        grid = [list(line) for line in pattern.splitlines()]

        def fold(grid, axis, offset) -> bool:

            if axis == 1:
                new_grid = []
                for i in range(len(grid[0])):
                    new_grid.append([row[i] for row in grid])
                grid = new_grid

            if offset < math.ceil(len(grid[0]) // 2):
                new_grid = []
                for row in grid:
                    new_grid.append(row[::-1])
                grid = new_grid
                offset = len(grid[0]) - offset -2

            num_incorrect = 0
            for i in range(len(grid)):
                right = grid[i][offset + 1:]
                left = (grid[i][:offset + 1])[-len(right):]
                if left != right[::-1]:
                    num_incorrect += 1
                    if num_incorrect > 1:
                        return False

            return num_incorrect == 1

        for axis in range(0, 2):
            limit = len(grid[0]) if axis == 0 else len(grid)
            for offset in range(limit - 1):
                if fold(grid, axis, offset):
                    if axis == 0:
                        total += offset + 1
                    else:
                        total += 100 * (offset + 1)
                    break
            else:
                continue
            break
        else:
            raise ValueError("no fold found")

    return total


for i, (data, solution) in enumerate(sample_data["A"], 1):
    if data == "" or solution is None:
        continue
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for A, {recived=} == {solution=}")
submit((answer := A(puzzle_data)), part="a", day=13, year=2023)
print(f"submitted {answer=} for part A")

for i, (data, solution) in enumerate(sample_data["B"], 1):
    if data == "" or solution is None:
        continue
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for B, {recived=} == {solution=}")
submit((answer := B(puzzle_data)), part="b", day=13, year=2023)
print(f"submitted {answer=} for part B")
