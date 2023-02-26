#!/usr/bin/env python3
"""This module defines the command interpreter for the HBNB console."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the HBNB console."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

