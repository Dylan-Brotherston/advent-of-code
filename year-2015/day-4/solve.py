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


data: str = clean(get_data(year=2015, day=4))
sample_data: str = clean("""
abcdef
""")


def A(input: str) -> int:
    import _md5
    for i in it.count():
        d = _md5.md5(f"{input}{i}".encode()).hexdigest()
        if d.startswith('0' * 5):
            return i


def B(input: str) -> int:
    import _md5
    for i in it.count():
        d = _md5.md5(f"{input}{i}".encode()).hexdigest()
        if d.startswith('0' * 6):
            return i


assert A(sample_data) == 609043, A(sample_data)
submit(A(data), part="a", day=4, year=2015)

assert B(sample_data) == 6742839, B(sample_data)
submit(B(data), part="b", day=4, year=2015)
