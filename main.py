import linewheel as lw

if __name__ == '__main__':
    function = lw.Function(name='1', fn=lambda arg: print("Hello, World!" + arg))
    subprocess = lw.Subprocess(name='2', command='ls -la')

    with lw.CommandLineInterface.builder() as builder:
        builder.command(function)
        builder.command(subprocess)

    cli = builder.build()
    cli.loop()
