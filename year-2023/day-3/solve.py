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


puzzle_data: str = clean(get_data(year=2023, day=3))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""), 4361),
    ],
    "B": [
        (clean("""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""), 467835),
    ],
}


def A(input: str) -> int:
    # create a grid
    gid = defaultdict(dict)
    for i, line in enumerate(input.splitlines()):
        for j, c in enumerate(line):
            gid[i][j] = c

    # find the coordinates of the symbols
    syms = []
    for i in gid.keys():
        for j in gid.keys():
            if gid[i][j] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                syms.append((i, j))

    # find the coordinates of numbers
    nums = []
    for i in gid.keys():
        for j in gid.keys():
            if gid[i][j] in digits:
                run = []
                dig = []
                for delta_j in count():
                    try:
                        if gid[i][j + delta_j] not in digits:
                            break
                        run.append((i, j + delta_j))
                        dig.append(gid[i][j + delta_j])
                        gid[i][j + delta_j] = "."  # remove the number so it doesn't get counted again
                    except KeyError:
                        break
                nums.append((int("".join(dig)), run))

    # find any numers that are adjacent to a symbol (including diagonals)
    adj = []
    for num, run in nums:
        end = False
        for i, j in run:
            for di, dj in product([-1, 0, 1], repeat=2):
                if (i + di, j + dj) in syms:
                    adj.append(num)
                    end = True
                    break
            if end:
                break

    return sum(adj)



def B(input: str) -> int:
    # create a grid
    gid = defaultdict(dict)
    for i, line in enumerate(input.splitlines()):
        for j, c in enumerate(line):
            gid[i][j] = c

    # find the coordinates of the symbols
    syms = []
    for i in gid.keys():
        for j in gid.keys():
            if gid[i][j] == "*":
                syms.append((i, j))

    # find the coordinates of numbers
    nums = []
    for i in gid.keys():
        for j in gid.keys():
            if gid[i][j] in digits:
                run = []
                dig = []
                for delta_j in count():
                    try:
                        if gid[i][j + delta_j] not in digits:
                            break
                        run.append((i, j + delta_j))
                        dig.append(gid[i][j + delta_j])
                        gid[i][j + delta_j] = "."  # remove the number so it doesn't get counted again
                    except KeyError:
                        break
                nums.append((int("".join(dig)), run))

    # find any * that is next two exactly two numbers
    adj = []
    for i, j in syms:
        n = []
        end = False
        for num, run in nums:
            for di, dj in product([-1, 0, 1], repeat=2):
                if (i + di, j + dj) in run:
                    n.append(num)
                    end = True
                    break
            if end:
                end = False

        if len(n) == 2:
            adj.append(n[0] * n[1])

    return sum(adj)


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=3, year=2023)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=3, year=2023)
