#! /usr/bin/env python3

import itertools as it
import more_itertools as mit
import functools as ft
import regex as re
import numpy as np
import urllib3 as ul
import dateutil.parser as dp

from aocd import get_data, submit # type: ignore

from share import *


PLACEHOLDER: object = object()


data: str = clean(get_data(year=2015, day=5))
sample_data: str = clean("""
ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
""")


def A(input: str) -> int:
    from collections import Counter
    total = 0
    for line in by_lines(input):
        C = Counter(line)
        if C['a'] + C['e'] + C['i'] + C['o'] + C['u'] < 3:
            continue
        if re.match(r'.*(.)\1.*', line) is None:
            continue
        if re.match(r'.*(ab|cd|pq|xy).*', line):
            continue
        total += 1
    return total


def B(input: str) -> int:
    total = 0
    for line in by_lines(input):
        if re.match(r'.*(..).*\1.*', line) is None:
            continue
        if re.match(r'.*(.).\1.*', line) is None:
            continue
        total += 1
    return total


assert A(sample_data) == 2, A(sample_data)
submit(A(data), part="a", day=5, year=2015)

assert B(sample_data) == 0, B(sample_data)
submit(B(data), part="b", day=5, year=2015)
