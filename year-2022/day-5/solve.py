#! /usr/bin/env python3

import itertools as it
import more_itertools as mit
import functools as ft
import regex as re
import numpy as np
import urllib3 as ul
import collections as cl
import dateutil.parser as dp

from aocd import get_data, submit  # type: ignore

from share import *


PLACEHOLDER: object = object()


data: str = clean(get_data(year=2022, day=5))
sample_data: str = clean(
    """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
)


def A(input: str) -> str:
    init, moves = by_paragraphs(input)
    stacks = cl.defaultdict(list)
    for line in by_lines(init)[:-1]:
        match = re.fullmatch(r"[[ ](.)[] ](?: [[ ](.)[] ])*", line)
        for index, letter in enumerate(match.captures(1) + match.captures(2), 1):
            if letter != " ":
                stacks[index].insert(0, letter)

    for move in by_lines(moves):
        match = re.fullmatch(r"move (\d+) from (\d+) to (\d+)", move)
        num, src, dst = map(int, match.groups())
        for _ in range(num):
            stacks[dst].append(stacks[src].pop())

    return "".join(map(lambda x: x[1][-1], sorted(stacks.items(), key=lambda x: x[0])))


def B(input: str) -> str:
    init, moves = by_paragraphs(input)
    stacks = cl.defaultdict(list)
    for line in by_lines(init)[:-1]:
        match = re.fullmatch(r"[[ ](.)[] ](?: [[ ](.)[] ])*", line)
        for index, letter in enumerate(match.captures(1) + match.captures(2), 1):
            if letter != " ":
                stacks[index].insert(0, letter)

    for move in by_lines(moves):
        match = re.fullmatch(r"move (\d+) from (\d+) to (\d+)", move)
        num, src, dst = map(int, match.groups())
        stacks[dst] += stacks[src][-num:]
        stacks[src] = stacks[src][:-num]

    return "".join(map(lambda x: x[1][-1], sorted(stacks.items(), key=lambda x: x[0])))


assert A(sample_data) == "CMZ", A(sample_data)
submit(A(data), part="a", day=5, year=2022)

assert B(sample_data) == "MCD", B(sample_data)
submit(B(data), part="b", day=5, year=2022)
