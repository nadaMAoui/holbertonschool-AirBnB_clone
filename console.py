import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
