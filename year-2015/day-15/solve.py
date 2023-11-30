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
from collections import Counter, defaultdict, namedtuple, deque
from aocd import get_data, submit  # type: ignore
from share import *


puzzle_data: str = clean(get_data(year=2015, day=15))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
            Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
            Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
        """), 62842880),
    ],
    "B": [
        (clean("""
            Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
            Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
        """), 57600000),
    ],
}


def A(input: str) -> int:
    ingredients = {}
    for line in input.splitlines():
        m = re.fullmatch(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", line)
        ingredients[m[1]] = tuple(map(int, m[2:]))

    def score(names: tuple[str]) -> int:
        properties = tuple(map(sum, zip(*(ingredients[name] for name in names))))
        return ft.reduce(lambda x, y: x * y, (max(0, p) for p in properties[:-1]))

    return max(score(quantities) for quantities in it.combinations_with_replacement(list(ingredients.keys()), 100))


def B(input: str) -> int:
    ingredients = {}
    for line in input.splitlines():
        m = re.fullmatch(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", line)
        ingredients[m[1]] = tuple(map(int, m[2:]))

    def score(names: tuple[str]) -> int:
        properties = tuple(map(sum, zip(*(ingredients[name] for name in names))))
        if properties[-1] != 500:
            return 0
        return ft.reduce(lambda x, y: x * y, (max(0, p) for p in properties[:-1]))

    return max(score(quantities) for quantities in it.combinations_with_replacement(list(ingredients.keys()), 100))


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=15, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=15, year=2015)
