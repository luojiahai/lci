import abc
from typing import Callable


class Command(abc.ABC):

    def __init__(self, name: str, fn: Callable) -> None:
        self.name = name
        self.fn = Command.function(fn)

    @staticmethod
    def function(fn) -> Callable[[str], bool]:
        def wrapper(arg) -> bool:
            fn(arg)
            print()
            return False
        return wrapper
