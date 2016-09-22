from typing import Iterable


def greeting(name):
    """Generate a greeting

    :param name: name of someone
    :type name: str
    :return: generated message
    :rtype: str
    """
    return "Hello, {}!".format(name)


def greeting_all(names: Iterable[str]) -> str:
    return "Hello, {}!".format(", ".join(names))
