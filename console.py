#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    command interpreter class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + spaces + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj = storage.get(args[0], args[1])
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj = storage.get(args[0], args[1])
            if obj is None:
                print("** no instance found **")
            else:
                storage.delete(obj)
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            class_objects = [str(obj) for obj in objects.values()
                             if type(obj).__name__ == arg]
            print(class_objects)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = storage.get(args[0], args[1])
            if obj is None:
                print("** no instance found **")
            else:
                setattr(obj, args[2], args[3])
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
