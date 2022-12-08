#! /usr/bin/env python3

import itertools as it
import more_itertools as mit
import functools as ft
import regex as re
import numpy as np
import urllib3 as ul
import dateutil.parser as dp

from aocd import get_data, submit  # type: ignore

from share import *


PLACEHOLDER: object = object()


data: str = clean(get_data(year=2022, day=8))
sample_data: str = clean(
    """
30373
25512
65332
33549
35390
"""
)


def A(input: str) -> int:
    grid = [to_ints(by_chars(line)) for line in by_lines(input)]

    total = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            seen = [True, True, True, True]
            for k in range(len(grid)):
                for l in range(len(grid[0])):
                    if i == k and j == l:
                        continue
                    if k == i and l < j and grid[k][l] >= col:
                        seen[0] = False
                    if k == i and l > j and grid[k][l] >= col:
                        seen[1] = False
                    if k < i and l == j and grid[k][l] >= col:
                        seen[2] = False
                    if k > i and l == j and grid[k][l] >= col:
                        seen[3] = False
            if any(seen):
                total += 1
    return total


def B(input: str) -> int:
    grid = [to_ints(by_chars(line)) for line in by_lines(input)]

    total = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            seen = [0, 0, 0, 0]
            for n in reversed(range(0, i)):
                seen[0] += 1
                if grid[n][j] >= col:
                    break
            for n in range(i + 1, len(grid)):
                seen[1] += 1
                if grid[n][j] >= col:
                    break
            for n in reversed(range(0, j)):
                seen[2] += 1
                if grid[i][n] >= col:
                    break
            for n in range(j + 1, len(grid[0])):
                seen[3] += 1
                if grid[i][n] >= col:
                    break
            t = ft.reduce(lambda x, y: x * y, seen)
            total = max(total, t)
    return total


assert A(sample_data) == 21, A(sample_data)
submit(A(data), part="a", day=8, year=2022)

assert B(sample_data) == 8, B(sample_data)
submit(B(data), part="b", day=8, year=2022)
