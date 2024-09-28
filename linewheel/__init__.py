from __future__ import annotations
import cmd
from typing import List
from linewheel.command import Command, Function, Subprocess


class Cmd(cmd.Cmd):

    def __init__(self) -> None:
        super().__init__()

    def get_names(self):
        # This returns a list of all methods of the class
        # including the dynamically added
        return dir(self)


class CommandLineInterface:

    def __init__(self, builder: Builder) -> None:
        self._cmd = Cmd()
        for command in builder._commands:
            setattr(self._cmd, f'do_{command.name}', command.fn)
            setattr(self._cmd, f'help_{command.name}', command.help)

    @staticmethod
    def builder() -> Builder:
        return CommandLineInterface.Builder()
    
    def loop(self):
        self._cmd.cmdloop()

    def onecmd(self, line: str):
        self._cmd.onecmd(line)

    def help(self):
        return self._cmd.do_help(None)

    class Builder:

        def __init__(self) -> None:
            self._commands: List[Command] = []

        def __enter__(self) -> CommandLineInterface.Builder:
            return self

        def __exit__(self, exc_type, exc_value, traceback) -> None:
            pass

        def command(self, command: Command) -> None:
            self._commands.append(command)

        def build(self) -> CommandLineInterface:
            return CommandLineInterface(self)
