from mocli.command import Command, executable
from typing import Callable


class Function(Command):

    def __init__(self, name: str, fn: Callable) -> None:
        super().__init__(name, executable(fn))
