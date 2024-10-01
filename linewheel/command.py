import abc
import subprocess
from typing import Callable, List


def command(executable: Callable[[List[str]], None]) -> Callable[[List[str]], bool]:
    def wrapper(args: List[str]) -> bool:
        executable(args)
        return False
    return wrapper


class Command(abc.ABC):

    def __init__(self, name: str, fn: Callable[[List[str]], bool]) -> None:
        self.name = name
        self.fn = fn


class Subprocess(Command):

    def __init__(self, name: str, line: str) -> None:
        fn = lambda args: subprocess.run(line.split())
        super().__init__(name, command(fn))
