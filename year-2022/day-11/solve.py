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


data: str = clean(get_data(year=2022, day=11))
sample_data: str = clean(
    """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
)


def A(input: str) -> int:
    monkeys = []
    inspect = []
    for monkey in by_paragraphs(input):
        atters = by_lines(monkey)
        items = [int(i) for i in atters[1].split(":")[1].split(",")]
        operation = atters[2].split("=")[1].strip()
        test = int(atters[3].split()[3].strip())
        if_true = int(atters[4].split()[5].strip())
        if_false = int(atters[5].split()[5].strip())
        monkeys.append((items, operation, test, if_true, if_false))
        inspect.append(0)


    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            items, operation, test, if_true, if_false = monkey
            while items:
                inspect[i] += 1
                old = items.pop(0)
                new = eval(operation)
                new //= 3
                if new % test:
                    monkeys[if_false][0].append(new)
                else:
                    monkeys[if_true][0].append(new)

    inspect.sort()

    return inspect[-1] * inspect[-2]


def B(input: str) -> int:
    monkeys = []
    inspect = []
    for monkey in by_paragraphs(input):
        atters = by_lines(monkey)
        items = [int(i) for i in atters[1].split(":")[1].split(",")]
        operation = atters[2].split("=")[1].strip()
        test = int(atters[3].split()[3].strip())
        if_true = int(atters[4].split()[5].strip())
        if_false = int(atters[5].split()[5].strip())
        monkeys.append((items, operation, test, if_true, if_false))
        inspect.append(0)

    lcm = np.lcm.reduce([i[2] for i in monkeys])

    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            items, operation, test, if_true, if_false = monkey
            while items:
                inspect[i] += 1
                old = items.pop(0)
                new = eval(operation)
                new %= lcm
                if new % test:
                    monkeys[if_false][0].append(new)
                else:
                    monkeys[if_true][0].append(new)

    inspect.sort()

    return inspect[-1] * inspect[-2]


assert A(sample_data) == 10605, A(sample_data)
submit(A(data), part="a", day=11, year=2022)

assert B(sample_data) == 2713310158, B(sample_data)
submit(B(data), part="b", day=11, year=2022)
