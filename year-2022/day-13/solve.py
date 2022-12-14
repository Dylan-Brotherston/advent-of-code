#! /usr/bin/env python3

import itertools as it
import more_itertools as mit
import functools as ft
import regex as re
import numpy as np
import urllib3 as ul
import dateutil.parser as dp
import json

from aocd import get_data, submit  # type: ignore

from share import *


PLACEHOLDER: object = object()


data: str = clean(get_data(year=2022, day=13))
sample_data: str = clean(
    """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""
)


def evaluate(lhs, rhs):
    if isinstance(lhs, int) and isinstance(rhs, int):
        return rhs - lhs

    if isinstance(lhs, list) and isinstance(rhs, list):
        for l, r in it.zip_longest(lhs, rhs, fillvalue=None):
            if l is None:
                return 1
            if r is None:
                return -1
            a = evaluate(l, r)
            if a != 0:
                return a
        return 0

    if isinstance(lhs, list) and isinstance(rhs, int):
        return evaluate(lhs, [rhs])

    if isinstance(lhs, int) and isinstance(rhs, list):
        return evaluate([lhs], rhs)

    assert False, (type(lhs), type(rhs))


def A(input: str) -> int:
    total = 0
    pairs = by_paragraphs(input)
    for i, pair in enumerate(pairs, 1):
        lhs, rhs = by_lines(pair)
        lhs, rhs = json.loads(lhs), json.loads(rhs)
        if evaluate(lhs, rhs) > 0:
            total += i

    return total


def B(input: str) -> int:
    packets = by_lines(input)
    packets = lfilter(None, packets)
    packets = lmap(json.loads, packets)
    packets.append([[2]])
    packets.append([[6]])
    sorted_packets = sorted(packets, key=ft.cmp_to_key(evaluate), reverse=True)
    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)


assert A(sample_data) == 13, A(sample_data)
submit(A(data), part="a", day=13, year=2022)

assert B(sample_data) == 140, B(sample_data)
submit(B(data), part="b", day=13, year=2022)
