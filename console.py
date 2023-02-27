#!/usr/bin/python3
"""
Program that contain the entry point of the command interpreter
"""

from models.user import User


class HBNBCommand(cmd.Cmd):
    ...
    
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User}
    
    def do_create(self, arg):
        ...
        
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_obj = HBNBCommand.classes[args[0]]
            obj = class_obj()
            for attr in attrs:
                key, value = attr.split("=")
                setattr(obj, key, value)
            obj.save()
            print(obj.id)
            
    def do_show(self, arg):
        ...
        
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        objects = models.storage.all(HBNBCommand.classes[args[0]])
        obj_id = "{}.{}".format(args[0], args[1])
        if obj_id not in objects:
            print("** no instance found **")
            return
        print(objects[obj_id])
        
    def do_destroy(self, arg):
        ...
        
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        objects = models.storage.all(HBNBCommand.classes[args[0]])
        obj_id = "{}.{}".format(args[0], args[1])
        if obj_id not in objects:
            print("** no instance found **")
            return
        del objects[obj_id]
        models.storage.save()
        
    def do_all(self, arg):
        ...
        
        if not arg or arg in HBNBCommand.classes:
            objects = models.storage.all(HBNBCommand.classes.get(arg))
            print([str(obj) for obj in objects.values()])
        else:
            print("** class doesn't exist **")
            
    def do_update(self, arg):
        ...
        
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        objects = models.storage.all(HBNBCommand.classes[args[0]])
        obj_id = "{}.{}".format(args[0], args[1])
        if obj_id not in objects:
            print("** no instance found **")
            return
        obj = objects[obj_id]
        attrs = args[2:]
        for attr in attrs:
            key, value = attr.split("=")
            setattr(obj, key, value)
        obj.save()
