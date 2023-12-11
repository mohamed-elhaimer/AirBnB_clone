#!/usr/bin/python3
"""This module defines the entry point of the command interpreter.

It allows us to interactively and non-interactively:
    - create a data model
    - manage (create, update, destroy, etc) objects via a console / interpreter
    - store and persist objects to a file (JSON file)

Typical usage example:

    $ ./console
    (hbnb)

    (hbnb) help
    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit

    (hbnb)
    (hbnb) quit
    $
"""
import re
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

current_classes = {'BaseModel': BaseModel, 'User': User,
                   'Amenity': Amenity, 'City': City, 'State': State,
                   'Place': Place, 'Review': Review}
list_attribut = ["id", "created_at", "updated_at"]


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def precmd(self, line):

        return super().precmd(line)

    def do_quit(self, args):
        """quit commande to exit the programme
        """

        return True

    def do_EOF(self, line):
        """Inbuilt EOF command to gracefully catch errors.
        """

        print("")
        return True

    def do_help(self, arg):
        """To get help on a command, type help <topic>.
        """

        return super().do_help(arg)

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, args):
        """user creation"""
        args = args.split()
        if not valider_classname(args):
            return
        new_object = current_classes[args[0]]()
        new_object.save()
        print(new_object.id)

    def do_show(self, args):
        """show user"""
        args = args.split()
        if not valider_classname(args, True):
            return
        data = storage.all()
        key = f"{args[0]}.{args[1]}"
        my_object = data.get(key, None)
        if my_object is None:
            print("** no instance found **")
        else:
            print(my_object)

    def do_destroy(self, args):
        args = args.split()
        if not valider_classname(args, True):
            return
        data = storage.all()
        key = f"{args[0]}.{args[1]}"
        my_object = data.get(key, None)
        if my_object is None:
            print("** no instance found **")
            return
        del data[key]
        storage.save()

    def do_all(self, args):
        args = args.split()
        all_objects = storage.all()
        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_objects.items()])
            return
        if args[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(str(v)) for _, v in all_objects.items()
                   if type(v).__name__ == args[0]])
            return

    def do_update(self, arg):
        args = arg.split()
        args = args[:4]
        if not valider_classname(args, True):
            return
        if not valider_att(args):
            return
        data = storage.all()
        key = f"{args[0]}.{args[1]}"
        my_object = data.get(key, None)
        if my_object is None:
            print("** no instance found **")
            return
        if args[2] in list_attribut:
            return
        first_attr = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if first_attr:
            setattr(my_object, args[2], first_attr[0])
        else:
            value_list = args[3].split()
            setattr(my_object, args[2], parse_str(value_list[0]))
        storage.save()


def valider_classname(args, check_id=False):
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in current_classes.keys():
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    return True


def valider_att(args):
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    if len(args) < 4:
        print("** value missing **")
        return False
    return True


def parse_str(arg):
    """Parse `arg` to an `int`, `float` or `string`.
    """
    parsed = re.sub("\"", "", arg)
    if is_int(parsed):
        return int(parsed)
    elif is_float(parsed):
        return float(parsed)
    else:
        return arg


def is_float(x):
    """Checks if `x` is float.
    """
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True


def is_int(x):
    """Checks if `x` is int.
    """
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


if __name__ == '__main__':
    HBNBCommand().cmdloop()
