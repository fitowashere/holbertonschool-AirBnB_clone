#!/usr/bin/python3
"""Module for the console"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Class for the console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand().class_dict.keys():
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            all_keys = storage.all()
            key = args[0] + "." + args[1]

            if key not in all_keys.keys():
                print("** no instance found **")

            else:
                print(all_keys[key])

    def do_destroy(self, line):
        """Deletes an instance"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand().class_dict.keys():
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            all_keys = storage.all()
            key = args[0] + "." + args[1]

            if key not in all_keys.keys():
                print("** no instance found **")

            else:
                del all_keys[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representations based or not on the class name"""
        args = line.split()

        if len(args) == 0:
            print([str(v) for v in storage.all().values()])

        elif args[0] not in HBNBCommand().class_dict.keys():
            print("** class doesn't exist **")

        else:
            print([str(v) for v in storage.all().values()
                  if v.__class__.__name__ == args[0]])


    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
