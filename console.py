#!/usr/bin/env python3
"""
This module defines the HBNBCommand class, a command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class implements a command interpreter with a custom prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty line + ENTER.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
