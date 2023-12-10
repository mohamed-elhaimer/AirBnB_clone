import cmd
import sys

from models.base_model import BaseModel
from models import storage

current_classes = {'BaseModel': BaseModel}

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
        if not valider_classname(args, False):
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
        key =f"{args[0]}.{args[1]}"
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
        key =f"{args[0]}.{args[1]}"
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
            print(["{}".format(str(v)) for _, v in  all_objects.items()])
            return
        if args[0] not in current_classes.keys():
            print("class doesn't exist")
            return
        else:
            print(["{}".format(str(v)) for _, v in  all_objects.items() if type(v).__name__ == args[0]])
            return
def valider_classname(args, check_id = False):
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in current_classes.keys():
        print("class doesn't exist")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()