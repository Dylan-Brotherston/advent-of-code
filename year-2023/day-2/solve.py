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
from functools import cache, lru_cache, reduce
from aocd import get_data, submit  # type: ignore
from pprint import pprint
from share import *


puzzle_data: str = clean(get_data(year=2023, day=2))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""), 8),
    ],
    "B": [
        (clean("""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""), 2286),
    ],
}

r = r"Game (?P<game_number>\d+): (?P<hand>(?P<cubes>(?P<count>\d+) (?P<colour>\w+))(, (?P<cubes>(?P<count>\d+) (?P<colour>\w+)))*)(?:; (?P<hand>(?P<cubes>(?P<count>\d+) (?P<colour>\w+))(, (?P<cubes>(?P<count>\d+) (?P<colour>\w+)))*))*"

def A(input: str) -> int:
    limits = { "red": 12, "green": 13, "blue": 14 }

    total = 0

    for game in input.splitlines():
        captures = re.fullmatch(r, game).capturesdict()

        for count, colour in lzip(captures["count"], captures["colour"]):
            if int(count) > limits[colour.strip()]:
                break
        else:
            total += int(captures["game_number"][0])

    return total



def B(input: str) -> int:
    total = 0

    for game in input.splitlines():
        captures = re.fullmatch(r, game).capturesdict()
        limits = { "red": None, "green": None, "blue": None }

        for count, colour in lzip(captures["count"], captures["colour"]):
            limits[colour.strip()] = max(limits[colour.strip()], int(count)) if limits[colour.strip()] is not None else int(count)

        total += prod(limits.values())

    return total


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=2, year=2023)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=2, year=2023)
