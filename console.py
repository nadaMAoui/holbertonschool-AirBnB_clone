#!/usr/bin/python3
"""Command interpreter for HBNB project"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
