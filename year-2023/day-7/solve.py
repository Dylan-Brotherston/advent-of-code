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


puzzle_data: str = clean(get_data(year=2023, day=7))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""), 6440),
    ],
    "B": [
        (clean("""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""), 5905),
    ],
}


@dataclass
class Cards(object):
    hand: list[int]
    bet: int


def A(input: str) -> int:
    game: list[Cards] = []
    for line in input.splitlines():
        hand, bet = line.split()
        hand = list(hand)
        new_hand = []
        for h in hand:
            if h == "T":
                new_hand.append(10)
            elif h == "J":
                new_hand.append(11)
            elif h == "Q":
                new_hand.append(12)
            elif h == "K":
                new_hand.append(13)
            elif h == "A":
                new_hand.append(14)
            else:
                new_hand.append(int(h))
        game.append(Cards(new_hand, int(bet)))

    def poker_sort(A, B):
        cA = Counter(A.hand)
        sA = None
        if cA.most_common(1)[0][1] == 5:
            # Five of a kind
            sA = 7
        elif cA.most_common(1)[0][1] == 4:
            # Four of a kind
            sA = 6
        elif cA.most_common(1)[0][1] == 3 and cA.most_common(2)[1][1] == 2:
            # Full house
            sA = 5
        elif cA.most_common(1)[0][1] == 3:
            # Three of a kind
            sA = 4
        elif cA.most_common(1)[0][1] == 2 and cA.most_common(2)[1][1] == 2:
            # Two pair
            sA = 3
        elif cA.most_common(1)[0][1] == 2:
            # One pair
            sA = 2
        else:
            # High card
            sA = 1

        cB = Counter(B.hand)
        sB = None
        if cB.most_common(1)[0][1] == 5:
            # Five of a kind
            sB = 7
        elif cB.most_common(1)[0][1] == 4:
            # Four of a kind
            sB = 6
        elif cB.most_common(1)[0][1] == 3 and cB.most_common(2)[1][1] == 2:
            # Full house
            sB = 5
        elif cB.most_common(1)[0][1] == 3:
            # Three of a kind
            sB = 4
        elif cB.most_common(1)[0][1] == 2 and cB.most_common(2)[1][1] == 2:
            # Two pair
            sB = 3
        elif cB.most_common(1)[0][1] == 2:
            # One pair
            sB = 2
        else:
            # High card
            sB = 1

        if sA != sB:
            return sB - sA

        if A.hand[0] != B.hand[0]:
            return B.hand[0] - A.hand[0]

        if A.hand[1] != B.hand[1]:
            return B.hand[1] - A.hand[1]

        if A.hand[2] != B.hand[2]:
            return B.hand[2] - A.hand[2]

        if A.hand[3] != B.hand[3]:
            return B.hand[3] - A.hand[3]

        if A.hand[4] != B.hand[4]:
            return B.hand[4] - A.hand[4]

        return 0


    game.sort(key=cmp_to_key(poker_sort), reverse=True)

    score = 0
    for i, cards in enumerate(game, 1):
        score += cards.bet * i

    return score


def B(input: str) -> int:
    game: list[Cards] = []
    for line in input.splitlines():
        hand, bet = line.split()
        hand = list(hand)
        new_hand = []
        for h in hand:
            if h == "T":
                new_hand.append(10)
            elif h == "J":
                new_hand.append(1)
            elif h == "Q":
                new_hand.append(12)
            elif h == "K":
                new_hand.append(13)
            elif h == "A":
                new_hand.append(14)
            else:
                new_hand.append(int(h))
        game.append(Cards(new_hand, int(bet)))

    def poker_sort(A, B):
        sA = None
        for c in combinations_with_replacement([2,3,4,5,6,7,8,9,10,12,13,14], 5):
            cA = A.hand.copy()
            for i in range(5):
                if cA[i] == 1:
                    cA[i] = c[i]
            cA = Counter(cA)
            if cA.most_common(1)[0][1] == 5:
                # Five of a kind
                sA = 7 if sA is None else max(sA, 7)
            elif cA.most_common(1)[0][1] == 4:
                # Four of a kind
                sA = 6 if sA is None else max(sA, 6)
            elif cA.most_common(1)[0][1] == 3 and cA.most_common(2)[1][1] == 2:
                # Full house
                sA = 5 if sA is None else max(sA, 5)
            elif cA.most_common(1)[0][1] == 3:
                # Three of a kind
                sA = 4 if sA is None else max(sA, 4)
            elif cA.most_common(1)[0][1] == 2 and cA.most_common(2)[1][1] == 2:
                # Two pair
                sA = 3 if sA is None else max(sA, 3)
            elif cA.most_common(1)[0][1] == 2:
                # One pair
                sA = 2 if sA is None else max(sA, 2)
            else:
                # High card
                sA = 1 if sA is None else max(sA, 1)

        sB = None
        for c in combinations_with_replacement([2,3,4,5,6,7,8,9,10,12,13,14], 5):
            cB = B.hand.copy()
            for i in range(5):
                if cB[i] == 1:
                    cB[i] = c[i]
            cB = Counter(cB)
            if cB.most_common(1)[0][1] == 5:
                # Five of a kind
                sB = 7 if sB is None else max(sB, 7)
            elif cB.most_common(1)[0][1] == 4:
                # Four of a kind
                sB = 6 if sB is None else max(sB, 6)
            elif cB.most_common(1)[0][1] == 3 and cB.most_common(2)[1][1] == 2:
                # Full house
                sB = 5 if sB is None else max(sB, 5)
            elif cB.most_common(1)[0][1] == 3:
                # Three of a kind
                sB = 4 if sB is None else max(sB, 4)
            elif cB.most_common(1)[0][1] == 2 and cB.most_common(2)[1][1] == 2:
                # Two pair
                sB = 3 if sB is None else max(sB, 3)
            elif cB.most_common(1)[0][1] == 2:
                # One pair
                sB = 2 if sB is None else max(sB, 2)
            else:
                # High card
                sB = 1 if sB is None else max(sB, 1)

        if sA != sB:
            return sB - sA

        cA = Counter(A.hand)
        cB = Counter(B.hand)

        if A.hand[0] != B.hand[0]:
            return B.hand[0] - A.hand[0]

        if A.hand[1] != B.hand[1]:
            return B.hand[1] - A.hand[1]

        if A.hand[2] != B.hand[2]:
            return B.hand[2] - A.hand[2]

        if A.hand[3] != B.hand[3]:
            return B.hand[3] - A.hand[3]

        if A.hand[4] != B.hand[4]:
            return B.hand[4] - A.hand[4]

        return 0


    game.sort(key=cmp_to_key(poker_sort), reverse=True)

    score = 0
    for i, cards in enumerate(game, 1):
        score += cards.bet * i

    return score


for i, (data, solution) in enumerate(sample_data["A"], 1):
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for A, {recived=} == {solution=}")
submit((answer := A(puzzle_data)), part="a", day=7, year=2023)
print(f"submitted {answer=} for part A")

for i, (data, solution) in enumerate(sample_data["B"], 1):
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
    print(f"passed example {i} for B, {recived=} == {solution=}")
submit((answer := B(puzzle_data)), part="b", day=7, year=2023)
print(f"submitted {answer=} for part B")
