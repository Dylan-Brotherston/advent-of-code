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


puzzle_data: str = clean(get_data(year=2015, day=9))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
            London to Dublin = 464
            London to Belfast = 518
            Dublin to Belfast = 141
        """), 605),
    ],
    "B": [
        (clean("""
            London to Dublin = 464
            London to Belfast = 518
            Dublin to Belfast = 141
        """), 982),
    ],
}


def A(input: str) -> int:
    locations = set()
    distances = defaultdict(dict)
    for line in input.splitlines():
        a, _, b, _, c = line.split()
        locations.add(a)
        locations.add(b)
        distances[a][b] = int(c)
        distances[b][a] = int(c)

    length = sys.maxsize
    for items in it.permutations(locations):
        dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
        length = min(length, dist)

    return length



def B(input: str) -> int:
    locations = set()
    distances = defaultdict(dict)
    for line in input.splitlines():
        a, _, b, _, c = line.split()
        locations.add(a)
        locations.add(b)
        distances[a][b] = int(c)
        distances[b][a] = int(c)

    length = 0
    for items in it.permutations(locations):
        dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
        length = max(length, dist)

    return length

for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=9, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=9, year=2015)
