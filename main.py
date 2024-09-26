from mocli import CommandLineInterface
from mocli.command.function import Function
from mocli.command.subprocess import Subprocess

if __name__ == '__main__':
    function = Function(name='1', fn=lambda arg: print("Hello, World!"))
    subprocess = Subprocess(name='2', command='ls -la')

    with CommandLineInterface.builder(
        prompt='(my-cli) ',
    ) as builder:
        builder.command(function)
        builder.command(subprocess)

    builder.build().cmdloop()
