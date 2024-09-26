import subprocess
from mocli.command import Command


class Subprocess(Command):

    def __init__(self, name: str, command: str) -> None:
        fn = lambda arg: subprocess.run(command.split())
        super().__init__(name, Command.executable(fn))
