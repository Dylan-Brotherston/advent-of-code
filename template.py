#! /usr/bin/env python3

import itertools as it
import more_itertools as mit
import functools as ft
import regex as re
import numpy as np
import urllib3 as ul
import dateutil.parser as dp

from aocd import get_data, submit  # type: ignore

from share import *


PLACEHOLDER: object = object()


data: str = clean(get_data(year=${YEAR}, day=${DAY}))
sample_data: str = clean(
    """
"""
)


def A(input: str) -> int:
    return None


def B(input: str) -> int:
    return None


assert A(sample_data) == PLACEHOLDER, A(sample_data)
submit(A(data), part="a", day=${DAY}, year=${YEAR})

assert B(sample_data) == PLACEHOLDER, B(sample_data)
submit(B(data), part="b", day=${DAY}, year=${YEAR})
