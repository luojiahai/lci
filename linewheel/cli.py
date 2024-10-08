from __future__ import annotations
import argparse
from typing import Dict
from linewheel.command import Command


def cli() -> CommandLineInterface.Builder:
    return CommandLineInterface.builder()


class CommandLineInterface:

    def __init__(self, builder: Builder) -> None:
        parser = argparse.ArgumentParser(prog=builder._name)
        subparsers = parser.add_subparsers(dest='command')
        commands = builder._commands

        for key in commands.keys():
            command_parser = subparsers.add_parser(name=key, help=f'{key}')
            command_parser.add_argument('args', nargs='*', help='arguments for the command')

        try:
            parsed = parser.parse_args()
            commands[parsed.__getattribute__('command')].fn(parsed.__getattribute__('args'))
        except Exception:
            parser.print_help()

    @staticmethod
    def builder() -> Builder:
        return CommandLineInterface.Builder()

    class Builder:

        def __init__(self, name: str = 'lw') -> None:
            self._name = name
            self._commands: Dict[str, Command] = {}

        def __enter__(self) -> CommandLineInterface.Builder:
            return self

        def __exit__(self, exc_type, exc_value, traceback) -> None:
            pass

        def command(self, command: Command) -> None:
            self._commands[command.name] = command

        def build(self) -> CommandLineInterface:
            return CommandLineInterface(self)
