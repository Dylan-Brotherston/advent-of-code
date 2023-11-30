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


puzzle_data: str = clean(get_data(year=2015, day=14))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
    ],
    "B": [
    ],
}


def A(input: str) -> int:
    speeds = {}
    for line in input.splitlines():
        m = re.fullmatch(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
        speeds[m[1]] = tuple(map(int, m[2:]))

    state = {r: (0, 0, True) for r in speeds.keys()}

    for _ in range(2503):
        for r, (d, t, f) in state.items():
            if f:
                d += speeds[r][0]
            t += 1
            if t == speeds[r][1 if f else 2]:
                t = 0
                f = not f
            state[r] = (d, t, f)

    return max(d for d, _, _ in state.values())


def B(input: str) -> int:
    speeds = {}
    for line in input.splitlines():
        m = re.fullmatch(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
        speeds[m[1]] = tuple(map(int, m[2:]))

    state = {r: (0, 0, True, 0) for r in speeds.keys()}

    for _ in range(2503):
        for r, (d, t, f, p) in state.items():
            if f:
                d += speeds[r][0]
            t += 1
            if t == speeds[r][1 if f else 2]:
                t = 0
                f = not f
            state[r] = (d, t, f, p)

        m = max(d for d, _, _, _ in state.values())
        for r, (d, t, f, p) in state.items():
            if d == m:
                state[r] = (d, t, f, p + 1)
            else:
                state[r] = (d, t, f, p)

    return max(p for _, _, _, p in state.values())




for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=14, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=14, year=2015)
