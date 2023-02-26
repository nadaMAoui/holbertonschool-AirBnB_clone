#!/usr/bin/python3
"""
Command interpreter for AirBnB project
"""

import cmd
import sys
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Do nothing when empty line is entered
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id.
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        try:
            instance = models.storage.all()[args[0] + "." + args[1]]
            print(instance)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        try:
            del models.storage.all()[args[0] + "." + args[1]]
            models.storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        if not arg:
            print([str(obj) for obj in models.storage.all().values()])
        else:
            try:
                print([str(obj) for obj in models.storage.all()[arg].values()])
            except KeyError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        try:
            instance = models.storage.all()[args[0] + "." + args[1]]
        except KeyError:
            print("** no instance found **")
            return

        setattr(instance, args[2], type(getattr(instance, args[2]))(args[3]))
        models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
