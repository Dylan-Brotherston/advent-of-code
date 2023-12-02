from typing import Any, TypeVar, Optional

from collections import defaultdict
from functools import reduce
from operator import mul
from more_itertools import collapse


def clean(data: str) -> str:
    from textwrap import dedent

    return dedent(data.strip("\n"))

def ssplit(data: str, sep: str | None, maxsplit = -1) -> list[str]:
    return data.strip().split(sep, maxsplit)

def by_groups(data: str, _sep: Optional[str]) -> list[str]:
    return data.split(_sep)


def by_lines(data: str) -> list[str]:
    return by_groups(data, _sep="\n")


def by_paragraphs(data: str) -> list[str]:
    return by_groups(data, _sep="\n\n")


def by_words(data: str) -> list[str]:
    return by_groups(data, _sep=None)


def by_chars(data: str) -> list[str]:
    return list(data)


_U = TypeVar("_U")


def to_type(data: list[str], _type: type[_U]) -> list[_U]:
    return lmap(_type, data)


def to_ints(data: list[str]) -> list[int]:
    return to_type(data, _type=int)


def to_floats(data: list[str]) -> list[float]:
    return to_type(data, _type=float)

def irange(start: int, stop: int = None, step: int = 1) -> range:
    if stop is None:
        stop = start
        start = 0
    return range(start, stop + 1, step)


def lmap(*args, **kwargs) -> list[Any]:
    return list(map(*args, **kwargs))


def lfilter(*args, **kwargs) -> list[Any]:
    return list(filter(*args, **kwargs))


def lrange(*args, **kwargs) -> list[int]:
    return list(range(*args, **kwargs))


def lirange(*args, **kwargs) -> list[int]:
    return list(irange(*args, **kwargs))


def lzip(*args, **kwargs) -> list[tuple[Any, ...]]:
    return list(zip(*args, **kwargs))

def nested_split(data: str, *args):
    if not args:
        return data
    sep, *args = args
    return list(collapse(lmap(lambda x: nested_split(x, *args), data.split(sep))))


def prod(data: list[int]) -> int:
    return reduce(mul, data)

letters = {
    'A': clean("""
        .##.
        #..#
        #..#
        ####
        #..#
        #..#
    """),
    'B': [clean("""
        ###.
        #..#
        ###.
        #..#
        #..#
        ###.
    """), clean("""
        ###.
        #..#
        #..#
        ###.
        #..#
        ###.
    """)],
    'C': clean("""
        .##.
        #..#
        #...
        #...
        #..#
        .##.
    """),
    'D': clean("""
        ###.
        #..#
        #..#
        #..#
        #..#
        ###.
    """),
    'E': [clean("""
        ####
        #...
        ###.
        #...
        #...
        ####
    """), clean("""
        ####
        #...
        #...
        ###.
        #...
        ####
    """)],
    'F': [clean("""
        ####
        #...
        ###.
        #...
        #...
        #...
    """), clean("""
        ####
        #...
        #...
        ###.
        #...
        #...
    """)],
    'G': clean("""
        .##.
        #..#
        #...
        #.##
        #..#
        .###
    """),
    'H': [clean("""
        #..#
        #..#
        ####
        #..#
        #..#
        #..#
    """), clean("""
        #..#
        #..#
        #..#
        ####
        #..#
        #..#
    """)],
    'I': [clean("""
        .##.
        ..#.
        ..#.
        ..#.
        ..#.
        .##.
    """), clean("""
        .##.
        .#..
        .#..
        .#..
        .#..
        .##.
    """)],
    'J': clean("""
        ..##
        ...#
        ...#
        ...#
        #..#
        .##.
    """),
    'K': [clean("""
        #..#
        #.#.
        ##..
        #.#.
        #..#
        #..#
    """), clean("""
        #..#
        #..#
        #.#.
        ##..
        #.#.
        #..#
    """)],
    'L': clean("""
        #...
        #...
        #...
        #...
        #...
        ####
    """),
    'M': clean("""
    """),
    'N': clean("""
    """),
    'O': clean("""
        .##.
        #..#
        #..#
        #..#
        #..#
        .##.
    """),
    'P': clean("""
        ###.
        #..#
        #..#
        ###.
        #...
        #...
    """),
    'Q': clean("""
    """),
    'R': clean("""
        ###.
        #..#
        #..#
        ###.
        #.#.
        #..#
    """),
    'S': [clean("""
        .###
        #...
        .##.
        ...#
        ...#
        ###.
    """), clean("""
        .###
        #...
        #...
        .##.
        ...#
        ###.
    """)],
    'T': [clean("""
        ####
        ..#.
        ..#.
        ..#.
        ..#.
        ..#.
    """), clean("""
        ####
        .#..
        .#..
        .#..
        .#..
        .#..
    """)],
    'U': clean("""
        #..#
        #..#
        #..#
        #..#
        #..#
        .##.
    """),
    'V': clean("""
    """),
    'W': clean("""
    """),
    'X': clean("""
    """),
    'Y': clean("""
    """),
    'Z': clean("""
        ####
        ...#
        ..#.
        .#..
        #...
        ####
    """),
}

numbers = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "sixteen",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
    1000000: "million",
    1000000000: "billion",
    1000000000000: "trillion",
    1000000000000000: "quadrillion",
    1000000000000000000: "quintillion",
    1000000000000000000000: "sextillion",
    1000000000000000000000000: "septillion",
    1000000000000000000000000000: "octillion",
    1000000000000000000000000000000: "nonillion",
}

def ascii_to_text(ascii: str, padding = (0, 0)) -> str:
    """
    Convert ASCII art to a string
    """

    ascii = clean(ascii)
    lines = by_lines(ascii)
    height = len(lines)
    width = len(lines[0])
    result = ""
    for y in range(0, height, 6):
        for x in range(0, width, 4 + padding[0] + padding[1]):
            letter = ""
            for y2 in range(y, y + 6):
                for x2 in range(x + padding[0], x + 4 + padding[0]):
                    letter += lines[y2][x2]
                letter += "\n"
            for letter_name, letter_ascii in letters.items():
                if isinstance(letter_ascii, list):
                    if letter in letter_ascii:
                        result += letter_name
                        break
                else:
                    if letter == letter_ascii:
                        result += letter_name
                        break
            else:
                raise Exception(f"Could not find letter: {letter}")
        result += " "
    return result.strip()

def integer_to_text(number: int) -> str:
    """
    Convert an integer in to it's word representation.
    """
    ones = {
        0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
        7: 'seventy', 8: 'eighty', 9: 'ninety'}
    illions = {
        1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
        6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
        10: 'nonillion', 11: 'decillion'}

    def _join(*args: list[str]) -> str:
        return ' '.join(filter(bool, args))

    def _integer_to_text(i: int) -> str:
        def _divide(dividend, divisor, magnitude):
            return _join(
                _integer_to_text(dividend // divisor),
                magnitude,
                _integer_to_text(dividend % divisor),
            )

        if i < 20:
            return ones[i]
        if i < 100:
            return _join(tens[i // 10], ones[i % 10])
        if i < 1000:
            return _divide(i, 100, 'hundred')
        for illions_number, illions_name in illions.items():
            if i < 1000**(illions_number + 1):
                break
        return _divide(i, 1000**illions_number, illions_name)

    if number < 0:
        return _join('negative', _integer_to_text(-number))
    if number == 0:
        return 'zero'
    return _integer_to_text(number)


class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError( key )
        else:
            ret = self[key] = self.default_factory(key)
            return ret
