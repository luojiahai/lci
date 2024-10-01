import linewheel as lw
from typing import List


@lw.command
def hello(args: List[str]) -> None:
    print("Hello, World!", args)


if __name__ == '__main__':
    with lw.cli() as cli:
        cli.command(lw.Command(
            name='hello',
            fn=hello,
        ))
        cli.command(lw.Subprocess(
            name='ls',
            line='ls -la',
        ))
    cli.build()
