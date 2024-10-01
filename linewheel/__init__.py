from __future__ import annotations
from typing import Dict, List
from linewheel.command import command, Command, Subprocess


def cli() -> CommandLineInterface.Builder:
    return CommandLineInterface.builder()


class CommandLineInterface:

    def __init__(self, builder: Builder) -> None:
        self._commands = builder._commands
        pass

    def execute(self, command: str, args: List[str]) -> None:
        self._commands[command].fn(args)

    @staticmethod
    def builder() -> Builder:
        return CommandLineInterface.Builder()

    class Builder:

        def __init__(self) -> None:
            self._commands: Dict[str, Command] = {}

        def __enter__(self) -> CommandLineInterface.Builder:
            return self

        def __exit__(self, exc_type, exc_value, traceback) -> None:
            pass

        def command(self, command: Command) -> None:
            self._commands[command.name] = command

        def build(self) -> CommandLineInterface:
            return CommandLineInterface(self)
