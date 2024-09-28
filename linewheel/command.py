import abc
import subprocess
from typing import Callable


def command_function(executable) -> Callable[[str], bool]:
    def wrapper(arg) -> bool:
        executable(arg)
        return False
    return wrapper

def print_help(help: str | None) -> None:
    if help: print(help)


class Command(abc.ABC):

    def __init__(self, name: str, fn: Callable, help: str = None) -> None:
        self.name = name
        self.fn = fn
        self.help = lambda: print_help(help)


class Function(Command):

    def __init__(self, name: str, fn: Callable, help: str = None) -> None:
        super().__init__(name, command_function(fn), help)


class Subprocess(Command):

    def __init__(self, name: str, command: str, help: str = None) -> None:
        fn = lambda arg: subprocess.run(command.split())
        super().__init__(name, command_function(fn), help)
