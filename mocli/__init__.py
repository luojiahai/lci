import cmd

class Hello(cmd.Cmd):

    prompt = "(mocli) > "

    def do_hello(self, arg):
        print("hello")
    
    def do_exit(self, arg):
        print("bye")
        return True
    
    def preloop(self):
        return self.do_help('')

def run():
    Hello().cmdloop()
