import abc
from typing import Callable


def commandfn(fn) -> Callable[[str], bool]:
    def wrapper(arg) -> bool:
        fn(arg)
        print()
        return False
    return wrapper


class Command(abc.ABC):

    def __init__(self, name: str, fn: Callable) -> None:
        self.name = name
        self.fn = fn
