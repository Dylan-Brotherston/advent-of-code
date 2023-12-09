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


puzzle_data: str = clean(get_data(year=2023, day=5))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""), 35),
    ],
    "B": [
        (clean("""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""), 46),
    ],
}


@dataclass
class Map(object):
    destination_range_start: int
    source_range_start: int
    range_length: int


def A(input: str) -> int:
    parts = input.split("\n\n")

    seeds = lmap(int, parts.pop(0).splitlines()[0].split(" ")[1:])

    maps: list[list[Map]] = []
    for part in parts:
        lines = part.splitlines()[1:]
        maps.append([])
        for line in lines:
            maps[-1].append(Map(*map(int, line.split(" "))))

    final = []
    for seed in seeds:
        for m in maps:
            for mm in m:
                if seed >= mm.source_range_start and seed <= mm.source_range_start + mm.range_length :
                    seed = mm.destination_range_start + seed - mm.source_range_start
                    break

        final.append(seed)

    return min(final)


def B(input: str) -> int:
    def locations(intervals):
        for maps_block in input_maps.split("\n\n"):
            mappings = [[int(x) for x in rules.split()] for rules in maps_block.split("\n")[1:]]
            images = list()
            while intervals:
                x, y = intervals.pop()
                for mapping in mappings:
                    a, b, delta = mapping
                    c = b + delta - 1
                    t = b - a
                    if b <= x <= y <= c:
                        images.append((x - t, y - t))
                        break
                    elif b <= x <= c < y:
                        images.append((x - t, c - t))
                        intervals.append((c + 1, y))
                        break
                    elif x < b <= y <= c:
                        images.append((b - t, y - t))
                        intervals.append((x, b - 1))
                        break
                else:
                    images.append((x, y))
            intervals = images
        return intervals

    input_seeds, input_maps = input.split("\n\n", 1)

    seed_data = [int(x) for x in re.findall(r"\d+", input_seeds)]
    seed_intervals = [(x, x + d - 1) for x, d in zip(seed_data[::2], seed_data[1::2])]
    return min(min(locations(seed_intervals)))


for i, (data, solution) in enumerate(sample_data["A"], 1):
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for A, {recived=} == {solution=}")
submit((answer := A(puzzle_data)), part="a", day=5, year=2023)
print(f"submitted {answer=} for part A")

for i, (data, solution) in enumerate(sample_data["B"], 1):
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for B, {recived=} == {solution=}")
submit((answer := B(puzzle_data)), part="b", day=5, year=2023)
print(f"submitted {answer=} for part B")
