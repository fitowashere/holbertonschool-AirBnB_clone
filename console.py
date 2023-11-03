#!/usr/bin/python3
"""Module for the console"""
import argparse
import cmd
import json
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class for the console"""
    prompt = '(hbnb) '
    valid_class = ["BaseModel", "User", "Place", "State",
                   "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valid_class:
            print("** class doesn't exist **")
            return

        new_model = eval(arg)()
        new_model.save()
        print(new_model.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        li_arg = arg.split()
        try:
            model = storage.all()[f"{li_arg[0]}.{li_arg[1]}"]
            print(model)
        except KeyError:
            print("** no instance found **")
        except IndexError:
            if li_arg[0] not in self.valid_class:
                print("** class doesn't exist **")
            elif len(li_arg) == 1:
                print("** instance id missing **")
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance"""
        li_arg = arg.split()
        if not li_arg:
            print("** class name missing **")
        elif li_arg[0] not in self.valid_class:
            print("** class doesn't exist **")
        elif len(li_arg) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = f'{li_arg[0]}.{li_arg[1]}'
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations based or not on the class name"""
        if not arg:
            for obj in storage.all():
                print(storage.all()[obj].__str__())
            return

        try:
            cls_name = eval(arg).__name__
        except NameError:
            print("** class doesn't exist **")
            return

        for obj in storage.all():
            if obj.startswith(f"{cls_name}."):
                print(storage.all()[obj].__str__())

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        read_only_attrs = ['id', 'created_at', 'updated_at']

        if not arg:
            print("** class name missing **")
            return

        li_arg = arg.split()
        if li_arg[0] not in self.valid_class:
            print("** class doesn't exist **")
            return

        if len(li_arg) == 1:
            print("** instance id missing **")
            return

        key = li_arg[0] + "." + li_arg[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return

        if len(li_arg) == 2:
            print("** attribute name missing **")
            return

        if len(li_arg) == 3:
            print("** value missing **")
            return

        # Prevent update of id, created_at, and updated_at
        if li_arg[2] in read_only_attrs:
            print(f"** {li_arg[2]} attribute can't be updated **")
            return

        try:
            value = eval(li_arg[3])
        except NameError:
            value = li_arg[3]

        setattr(storage.all()[key], li_arg[2], value)
        print(f"Updated {li_arg[2]} to {value} in instance {key}")
        storage.all()[key].save()

    def emptyline(self):
        """Do nothing when hit enters\n"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
