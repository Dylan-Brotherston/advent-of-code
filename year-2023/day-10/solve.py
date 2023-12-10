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


puzzle_data: str = clean(get_data(year=2023, day=10))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
.....
.S-7.
.|.|.
.L-J.
.....
"""), 4),
        (clean("""
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""), 4),
        (clean("""
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""), 8),
        (clean("""
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""), 8),
    ],
    "B": [
        (clean("""
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""), 4),
        (clean("""
..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
"""), 4),
        (clean("""
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""), 8),
        (clean("""
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""), 10),
    ],
}


class Point(object):
    top: bool
    right: bool
    bottom: bool
    left: bool
    start: bool
    distance: int
    inside: bool | None

    def __init__(self, symbol: str) -> None:
        self.start = symbol == "S"
        self.distance = None

        self.top = symbol in "|LJ"
        self.bottom = symbol in "|F7"
        self.right = symbol in "-FL"
        self.left = symbol in "-7J"

        self.inside = None

    def directions(self) -> list[tuple[int, int]]:
        return (self.top, self.right, self.bottom, self.left)

def A(input: str) -> int:
    grid: list[list[Point]] = []

    for line in input.splitlines():
        grid.append([Point(symbol) for symbol in line])

    start = next((y, x) for y, row in enumerate(grid) for x, point in enumerate(row) if point.start)
    i, j = start

    if i + 0 >= 0 and i + 0 < len(grid) and j - 1 >= 0 and j - 1 < len(grid[i + 0]):
        if grid[i + 0][j - 1].right:
            grid[i][j].left = True
    if i + 0 >= 0 and i + 0 < len(grid) and j + 1 >= 0 and j + 1 < len(grid[i + 0]):
        if grid[i + 0][j + 1].left:
            grid[i][j].right = True
    if i - 1 >= 0 and i - 1 < len(grid) and j + 0 >= 0 and j + 0 < len(grid[i - 1]):
        if grid[i - 1][j + 0].bottom:
            grid[i][j].top = True
    if i + 1 >= 0 and i + 1 < len(grid) and j + 0 >= 0 and j + 0 < len(grid[i + 1]):
        if grid[i + 1][j + 0].top:
            grid[i][j].bottom = True

    queue = deque([(*start, 0)])
    while queue:
        i, j, distance = queue.popleft()
        point = grid[i][j]
        if point.distance is None or point.distance > distance:
            point.distance = distance
            if point.top and (i - 1, j) != start:
                queue.append((i - 1, j, distance + 1))
            if point.right and (i, j + 1) != start:
                queue.append((i, j + 1, distance + 1))
            if point.bottom and (i + 1, j) != start:
                queue.append((i + 1, j, distance + 1))
            if point.left and (i, j - 1) != start:
                queue.append((i, j - 1, distance + 1))

    return max(point.distance for row in grid for point in row if point.distance is not None)

def B(input: str) -> int:
    grid: list[list[Point]] = []
    for line in input.splitlines():
        grid.append([Point(symbol) for symbol in line])

    start = next((y, x) for y, row in enumerate(grid) for x, point in enumerate(row) if point.start)
    i, j = start

    if i + 0 >= 0 and i + 0 < len(grid) and j - 1 >= 0 and j - 1 < len(grid[i + 0]):
        if grid[i + 0][j - 1].right:
            grid[i][j].left = True
    if i + 0 >= 0 and i + 0 < len(grid) and j + 1 >= 0 and j + 1 < len(grid[i + 0]):
        if grid[i + 0][j + 1].left:
            grid[i][j].right = True
    if i - 1 >= 0 and i - 1 < len(grid) and j + 0 >= 0 and j + 0 < len(grid[i - 1]):
        if grid[i - 1][j + 0].bottom:
            grid[i][j].top = True
    if i + 1 >= 0 and i + 1 < len(grid) and j + 0 >= 0 and j + 0 < len(grid[i + 1]):
        if grid[i + 1][j + 0].top:
            grid[i][j].bottom = True

    queue = deque([(*start, 0)])
    while queue:
        i, j, distance = queue.popleft()
        point = grid[i][j]
        if point.distance is None or point.distance > distance:
            point.distance = distance
            if point.top and (i - 1, j) != start:
                queue.append((i - 1, j, distance + 1))
            if point.right and (i, j + 1) != start:
                queue.append((i, j + 1, distance + 1))
            if point.bottom and (i + 1, j) != start:
                queue.append((i + 1, j, distance + 1))
            if point.left and (i, j - 1) != start:
                queue.append((i, j - 1, distance + 1))

    for row in grid:
        for point in row:
            if point.distance is None:
                point.top = point.right = point.bottom = point.left = False

    new_grid = defaultdict(list)
    for i, row in enumerate(grid):
        for j, point in enumerate(row):
            match point.directions():
                case (False, False, False, False):
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 1].append(Point("."))
                    new_grid[(i * 3) + 1].append(Point("."))
                    new_grid[(i * 3) + 1].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("."))
                case (True, False, True, False):
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 0].append(Point("|"))
                    new_grid[(i * 3) + 0][-1].distance = point.distance
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 1].append(Point("."))
                    new_grid[(i * 3) + 1].append(Point("|"))
                    new_grid[(i * 3) + 1][-1].distance = point.distance
                    new_grid[(i * 3) + 1].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("|"))
                    new_grid[(i * 3) + 2][-1].distance = point.distance
                    new_grid[(i * 3) + 2].append(Point("."))
                case (False, True, False, True):
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 1].append(Point("-"))
                    new_grid[(i * 3) + 1][-1].distance = point.distance
                    new_grid[(i * 3) + 1].append(Point("-"))
                    new_grid[(i * 3) + 1][-1].distance = point.distance
                    new_grid[(i * 3) + 1].append(Point("-"))
                    new_grid[(i * 3) + 1][-1].distance = point.distance
                    new_grid[(i * 3) + 2].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("."))
                case (True, True, False, False):
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 0].append(Point("|"))
                    new_grid[(i * 3) + 0][-1].distance = point.distance
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 1].append(Point("."))
                    new_grid[(i * 3) + 1].append(Point("L"))
                    new_grid[(i * 3) + 1][-1].distance = point.distance
                    new_grid[(i * 3) + 1].append(Point("-"))
                    new_grid[(i * 3) + 1][-1].distance = point.distance
                    new_grid[(i * 3) + 2].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("."))
                case (False, True, True, False):
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 1].append(Point("."))
                    new_grid[(i * 3) + 1].append(Point("F"))
                    new_grid[(i * 3) + 1][-1].distance = point.distance
                    new_grid[(i * 3) + 1].append(Point("-"))
                    new_grid[(i * 3) + 1][-1].distance = point.distance
                    new_grid[(i * 3) + 2].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("|"))
                    new_grid[(i * 3) + 2][-1].distance = point.distance
                    new_grid[(i * 3) + 2].append(Point("."))
                case (False, False, True, True):
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 1].append(Point("-"))
                    new_grid[(i * 3) + 1][-1].distance = point.distance
                    new_grid[(i * 3) + 1].append(Point("7"))
                    new_grid[(i * 3) + 1][-1].distance = point.distance
                    new_grid[(i * 3) + 1].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("|"))
                    new_grid[(i * 3) + 2][-1].distance = point.distance
                    new_grid[(i * 3) + 2].append(Point("."))
                case (True, False, False, True):
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 0].append(Point("|"))
                    new_grid[(i * 3) + 0][-1].distance = point.distance
                    new_grid[(i * 3) + 0].append(Point("."))
                    new_grid[(i * 3) + 1].append(Point("-"))
                    new_grid[(i * 3) + 1][-1].distance = point.distance
                    new_grid[(i * 3) + 1].append(Point("J"))
                    new_grid[(i * 3) + 1][-1].distance = point.distance
                    new_grid[(i * 3) + 1].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("."))
                    new_grid[(i * 3) + 2].append(Point("."))
                case _:
                    raise ValueError(f"invalid point {point}")

    # dict[int, list[Point]] -> list[list[Point]]
    grid = [row for _, row in sorted(new_grid.items())]

    for i, row in enumerate(grid):
        for j, point in enumerate(row):
            if point.inside is None:
                seen = set()
                queue = set()
                queue.add((i, j))
                touch = False
                while queue:
                    i, j = queue.pop()
                    if (i, j) in seen:
                        continue
                    try:
                        point = grid[i][j]
                    except IndexError:
                        touch = True
                        continue
                    if point.distance is not None:
                        continue
                    seen.add((i, j))
                    queue.add((i - 1, j))
                    queue.add((i, j + 1))
                    queue.add((i + 1, j))
                    queue.add((i, j - 1))
                for i, j in seen:
                    grid[i][j].inside = not touch

    return sum(point.inside for i, row in enumerate(grid) for j, point in enumerate(row) if point.inside is not None and i % 3 == 1 and j % 3 == 1)



for i, (data, solution) in enumerate(sample_data["A"], 1):
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for A, {recived=} == {solution=}")
submit((answer := A(puzzle_data)), part="a", day=10, year=2023)
print(f"submitted {answer=} for part A")

for i, (data, solution) in enumerate(sample_data["B"], 1):
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for B, {recived=} == {solution=}")
submit((answer := B(puzzle_data)), part="b", day=10, year=2023)
print(f"submitted {answer=} for part B")
