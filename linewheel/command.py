import abc
import subprocess
from typing import Callable, List


def command_function(executable) -> Callable[[List[str]], bool]:
    def wrapper(args) -> bool:
        executable(args)
        return False
    return wrapper


class Command(abc.ABC):

    def __init__(self, name: str, fn: Callable[[List[str]], bool]) -> None:
        self.name = name
        self.fn = fn


class Function(Command):

    def __init__(self, name: str, fn: Callable[[List[str]], None]) -> None:
        super().__init__(name, command_function(fn))


class Subprocess(Command):

    def __init__(self, name: str, command: str) -> None:
        fn = lambda arg: subprocess.run(command.split())
        super().__init__(name, command_function(fn))
