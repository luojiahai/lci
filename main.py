import linewheel as lw
import argparse


@lw.command
def hello(args):
    print("Hello, World!", args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='lw')
    subparsers = parser.add_subparsers(dest='command')
    hello_parser = subparsers.add_parser(name='hello', help='this is a help for hello')
    hello_parser.add_argument('args', nargs='*', help='this is a help for args')
    ls_parser = subparsers.add_parser(name='ls', help='this is a help for ls')

    with lw.cli() as cli:
        cli.command(lw.Command(
            name='hello',
            fn=lambda args: print("Hello, World!", args),
        ))
        cli.command(lw.Subprocess(
            name='ls',
            line='ls -la',
        ))

    cli = cli.build()
    try:
        args = parser.parse_args()
        cli.execute(
            args.__getattribute__('command'),
            args.__getattribute__('args') if 'args' in args else None,
        )
    except Exception as e:
        print(e)
        parser.print_help()
