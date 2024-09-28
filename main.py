import linewheel as lw
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='lw', add_help=False)
    parser.add_argument('command', nargs='+')

    with lw.CommandLineInterface.builder() as builder:
        builder.command(lw.Function(
            name='hello',
            fn=lambda arg: print("Hello, World!" + arg),
            help='help',
        ))
        builder.command(lw.Subprocess(
            name='ls',
            command='ls -la',
            help='another help',
        ))

    cli = builder.build()
    try: 
        args = parser.parse_args()
        command = ' '.join(args.__getattribute__('command'))
        cli.onecmd(line=command)
    except:
        cli.help()
