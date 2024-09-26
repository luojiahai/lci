from __future__ import annotations
import cmd
from typing import List, Self
from mocli.command import Command, commandfn
from mocli.command.shell import Shell


class CommandLineInterface(cmd.Cmd):

    def __init__(self, builder: Builder) -> None:
        super().__init__()
        self.prompt = builder._prompt
        for command in builder._commands:
            setattr(self, f'do_{command.name}', command.fn)

    @staticmethod
    def builder() -> Builder:
        return CommandLineInterface.Builder()

    def get_names(self):
        # This returns a list of all methods of the class
        # including the dynamically added
        return dir(self)

    def do_exit(self, arg):
        print("bye")
        return True

    def preloop(self):
        return self.do_help('')

    class Builder:

        def __init__(self) -> None:
            self._prompt = "(mocli) "
            self._commands: List[Command] = []

        def prompt(self, prompt: str) -> Self:
            self._prompt = prompt
            return self

        def command(self, command: Command) -> Self:
            self._commands.append(command)
            return self

        def build(self) -> CommandLineInterface:
            return CommandLineInterface(self)


@commandfn
def hello_fn(arg):
    print("Hello, world! " + arg)


def run():
    hello = Command('hello', hello_fn)
    shell = Shell('ls', 'ls -la')
    cli = CommandLineInterface.builder() \
        .prompt("(my-cli) ") \
        .command(hello) \
        .command(shell) \
        .build()
    cli.cmdloop()
