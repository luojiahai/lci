import subprocess
from mocli.command import Command


class Subprocess(Command):

    def __init__(self, name: str, command: str) -> None:
        super().__init__(name, lambda arg: subprocess.run(command.split()))
