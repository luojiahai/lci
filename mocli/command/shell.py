import subprocess
from mocli.command import Command, commandfn


class Shell(Command):

    def __init__(self, name: str, command: str) -> None:
        @commandfn
        def execute(arg): subprocess.run(command.split())
        super().__init__(name, execute)
