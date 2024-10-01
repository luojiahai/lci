import linewheel as lw


@lw.command
def hello(args):
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
