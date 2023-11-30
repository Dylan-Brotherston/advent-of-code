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
import collections as coll

from textwrap import dedent, indent
from aocd import get_data, submit  # type: ignore
from share import *

sys.setrecursionlimit(10000)

puzzle_data: str = clean(get_data(year=2022, day=12))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""), 31),
    ],
    "B": [
        (clean("""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""), 29),
    ],
}


def print_grid(grid: np.ndarray, visited: dict[tuple[int, int], str]):
    """
    Print the grid with the visited path.
    """
    for i, row in enumerate(grid):
        for j, letter in enumerate(row):
            if (i, j) in visited.keys():
                print(visited[(i, j)], end="")
            else:
                print(letter, end="")
        print()

    print(len(visited))


def BFS(grid, start, end):
    """
    Find the length of the shortest path from S to E.
    only move up, down, left, right
    only move to a letter that is less than, or equal to, or one more then the current letter
    S is the starting point and is the same as a
    E is the ending point and is the same as z
    """

    values = {chr(i): i - (ord('a') - 1) for i in range(ord('a'), ord('a') + (ord('z') - ord('a')) + 1)}

    visited = set()
    queue = coll.deque()
    queue.append([start])

    while queue:
        path = queue.popleft()
        current = path[-1]
        current_height = values[grid[tuple(current)]]

        if tuple(current) in visited:
            continue

        visited.add(tuple(current))

        if tuple(current) == tuple(end):
            return len(path) - 1

        for delta in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            position = current + delta

            # if the position is out of bounds, skip it
            if any(position < 0) or any(position >= grid.shape):
                continue

            # if the new position is more then one higher then the current position, skip it
            position_height = values[grid[tuple(position)]]
            if position_height > current_height + 1:
                continue

            path_copy = path.copy()
            path_copy.append(position)
            queue.append(path_copy)

    return None


def A(input: str) -> int:
    # make a 2D grid from the input
    grid = np.array([list(line) for line in input.splitlines()])
    # find the starting point
    start = np.argwhere(grid == "S")[0]
    # find the ending point
    end = np.argwhere(grid == "E")[0]

    # make the starting point have height a
    grid[tuple(start)] = "a"
    # make the ending point have height z
    grid[tuple(end)] = "z"

    return BFS(grid, start, end)


def B(input: str) -> int:
    # make a 2D grid from the input
    grid = np.array([list(line) for line in input.splitlines()])
    # find the starting point
    start = np.argwhere(grid == "S")[0]
    # find the ending point
    end = np.argwhere(grid == "E")[0]

    # make the starting point have height a
    grid[tuple(start)] = "a"
    # make the ending point have height z
    grid[tuple(end)] = "z"

    # find all `a` points
    a_points = np.argwhere(grid == "a")
    lengths = []
    for a_point in a_points:
        lengths.append(BFS(grid, a_point, end))
        if lengths[-1] is None:
            lengths.pop()

    return min(lengths)


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=12, year=2022)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=12, year=2022)
