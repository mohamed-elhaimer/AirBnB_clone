import cmd
import sys

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

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
        if not valider_classname(args):
            return
        
        new_object = current_classes[args[0]]()
        new_object.save()
        print(new_object.id)
    
    def do_show(self, args):
        """show user"""
        
        args = args.split()
        if not valider_classname(args, check_id = True):
            return
        for key in FileStorage.__objects.keys():
            if key == f"{current_classes[args[0]]}.{args[1]}":
                print(FileStorage.__objects[key])
            else:
                print("** no instance found **")
def valider_classname(args, check_id = False):
    if args[0] not in current_classes.keys():
        print("class doesn't exist")
        return False
    if len(args) < 1:
        print("** class name missing **")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
    return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()