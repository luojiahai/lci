import linewheel as lw
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='lw')
    subparsers = parser.add_subparsers(dest='command')
    hello_parser = subparsers.add_parser(name='hello', help='this is a help for hello')
    hello_parser.add_argument('args', nargs='*', help='this is a help for args')
    ls_parser = subparsers.add_parser(name='ls', help='this is a help for ls')

    with lw.cli() as cli:
        cli.command(lw.Function(
            name='hello',
            fn=lambda args: print("Hello, World!", args),
        ))
        cli.command(lw.Subprocess(
            name='ls',
            command='ls -la',
        ))

    cli = cli.build()
    try:
        args = parser.parse_args()
        command = args.__getattribute__('command')
        cli.commands[command].fn(args.__getattribute__('args'))
    except Exception as e:
        print(e)
        parser.print_help()
