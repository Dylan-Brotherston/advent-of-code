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


puzzle_data: str = clean(get_data(year=2023, day=8))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""), 2),
        (clean("""
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""), 6),
    ],
    "B": [
#         (clean("""
# LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)
# """), 6),
    ],
}


def A(input: str) -> int:
    input = input.splitlines()
    steps = list(input.pop(0))
    input.pop(0)

    nodes: dict[str, tuple[str, str]] = {}
    for line in input:
        line = line.split(" = ")
        nodes[line[0]] = tuple(line[1].strip("()").split(", "))

    current = "AAA"
    num_steps = 0
    for step in cycle(steps):
        if current == "ZZZ":
            break

        num_steps += 1

        if step == "L":
            current = nodes[current][0]
        elif step == "R":
            current = nodes[current][1]

    return num_steps


def B(input: str) -> int:
    input = input.splitlines()
    steps = input.pop(0)
    input.pop(0)

    nodes: dict[str, tuple[str, str]] = {}
    for line in input:
        line = line.split(" = ")
        nodes[line[0]] = tuple(line[1].strip("()").split(", "))

    fast_forward_map = {}
    get_to_z_early_spots = set()
    for start in nodes:
        where = start
        for idx, todo in enumerate(steps):
            if idx > 0 and where.endswith("Z"):
                get_to_z_early_spots.add(start)
            if todo == "L":
                where = nodes[where][0]
            else:
                where = nodes[where][1]
        fast_forward_map[start] = where

    start_network = set(x for x in nodes if x.endswith("A"))
    ssize = 0
    while ssize < len(start_network):
        ssize = len(start_network)
        start_network.update(sorted(fast_forward_map[x] for x in start_network))

    if get_to_z_early_spots & start_network:
        raise ValueError(
            "Assumptions violated by these start_network places that get to '**Z' early:"
            + str(sorted(get_to_z_early_spots & start_network))
        )

    factors = []
    for start in [x for x in nodes if x.endswith("A")]:
        where = fast_forward_map[start]
        zjumps = []
        jumps = 1
        beenthere = {start: 0}
        while where not in beenthere:
            beenthere.update({where: jumps})
            if where.endswith("Z"):
                zjumps.append(jumps)
            where = fast_forward_map[where]
            jumps += 1
        if beenthere[where] != 1:
            raise ValueError(
                f"Assumptions violated: {start} loops back to restart at {beenthere[where]} at {where}"
            )
        if len(zjumps) != 1 or zjumps[0] != jumps - 1:
            raise ValueError(f"Assumptions violated: {zjumps} out of loop found at {jumps}")
        factors.append(jumps - 1)

    return len(steps) * math.lcm(*factors)


for i, (data, solution) in enumerate(sample_data["A"], 1):
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for A, {recived=} == {solution=}")
submit((answer := A(puzzle_data)), part="a", day=8, year=2023)
print(f"submitted {answer=} for part A")

for i, (data, solution) in enumerate(sample_data["B"], 1):
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for B, {recived=} == {solution=}")
submit((answer := B(puzzle_data)), part="b", day=8, year=2023)
print(f"submitted {answer=} for part B")
