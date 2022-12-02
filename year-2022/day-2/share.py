from typing import Any, TypeVar


def clean(data: str) -> str:
    from textwrap import dedent
    return dedent(data.strip('\n'))


def by_groups(data: str, _sep: str) -> list[str]:
    return data.split(_sep)

def by_lines(data: str) -> list[str]:
    return by_groups(data, _sep='\n')

def by_paragraphs(data: str) -> list[str]:
    return by_groups(data, _sep='\n\n')

def by_words(data: str) -> list[str]:
    return by_groups(data, _sep=' ')

def by_chars(data: str) -> list[str]:
    return by_groups(data, _sep='')


_U = TypeVar('_U')
def to_type(data: list[str], _type: type[_U]) -> list[_U]:
    return list(map(_type, data))

def to_int(data: list[str]) -> list[int]:
    return to_type(data, _type=int)

def to_float(data: list[str]) -> list[float]:
    return to_type(data, _type=float)


def lmap(*args, **kwargs) -> list[Any]:
    return list(map(*args, **kwargs))
