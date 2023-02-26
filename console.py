#!/usr/bin/python3
"""
This module defines the console for the HBnB project.
"""
import cmd
import json
import shlex
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class definition.
    """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        Exit the console.
        """
        print()
        return True

    def emptyline(self):
        """
        An empty line does nothing.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it (to the JSON file) and print the id.
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                args = shlex.split(arg)
                class_name = args[0]
                if class_name not in storage.classes.keys():
                    print("** class doesn't exist **")
                else:
                    instance = storage.classes[class_name]()
                    instance.save()
                    print(instance.id)
            except Exception as e:
                print(e)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                args = shlex.split(arg)
                class_name = args[0]
                if class_name not in storage.classes.keys():
                    print("** class doesn't exist **")
                elif len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = class_name + '.' + instance_id
                    if key not in storage.all().keys():
                        print("** no instance found **")
                    else:
                        instance = storage.all()[key]
                        print(instance)
            except Exception as e:
                print(e)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                args = shlex.split(arg)
                class_name = args[0]
                if class_name not in storage.classes.keys():
                    print("** class doesn't exist **")
                elif len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = class_name + '.' + instance_id
                    if key not in storage.all().keys():

if __name__ == '__main__':
    HBNBCommand().cmdloop()
