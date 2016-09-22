from typing import Tuple, TypeVar


def add(x: int, y: int) -> int:
    return x + y


def greeting(name: str) -> str:
    return "Hello, {}!".format(name)

T = TypeVar("T")
def make_pair(e: T) -> Tuple[T, T]:
    return e, e
