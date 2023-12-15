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


puzzle_data: str = clean(get_data(year=2023, day=15))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
HASH
"""), 52),
        (clean("""
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""), 1320),
    ],
    "B": [
        (clean("""
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""), 145),
    ],
}


def HASH(input: str, hash: int = 0) -> int:
    for char in input:
        hash += ord(char)
        hash *= 17
        hash %= 256
    return hash


def A(input: str) -> int:
    total = 0
    for step in input.split(","):
        total += HASH(step)
    return total


class Lens(object):
    label: str
    focal_length: int

    def __init__(self, label: str, focal_length: int = None):
        self.label = label
        self.focal_length = focal_length

    def __eq__(self, __value: object) -> bool:
        return self.label == __value.label

    def __str__(self) -> str:
        return f"[{self.label} {self.focal_length}]"


def B(input: str) -> int:
    boxes = [ [] for _ in range(256) ]

    for step in input.split(","):
        label, action, value = re.fullmatch(r"([a-z]+)([=-])(\d*)", step).groups()

        hash = HASH(label)
        if action == "=":
            if Lens(label) not in boxes[hash]:
                boxes[hash].append(Lens(label, int(value)))
            else:
                boxes[hash][boxes[hash].index(Lens(label))].focal_length = int(value)
        elif action == "-":
            if Lens(label) in boxes[hash]:
                boxes[hash].remove(Lens(label))

    total = 0
    for i, box in enumerate(boxes, 1):
        for j, lens in enumerate(box, 1):
            total += i * j * lens.focal_length

    return total

for i, (data, solution) in enumerate(sample_data["A"], 1):
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for A, {recived=} == {solution=}")
submit((answer := A(puzzle_data)), part="a", day=15, year=2023)
print(f"submitted {answer=} for part A")

for i, (data, solution) in enumerate(sample_data["B"], 1):
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for B, {recived=} == {solution=}")
submit((answer := B(puzzle_data)), part="b", day=15, year=2023)
print(f"submitted {answer=} for part B")
