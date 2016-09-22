from typing import List


def greeting(name: str) -> str:
    return "Hello, {}!".format(name)


def count_zero(elements: List[int]) -> int:
    return sum(1 for e in elements if e == 0)
