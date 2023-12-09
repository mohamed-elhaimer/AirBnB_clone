import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def do_quit(self, args):
        """quit commande to exit the programme"""
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
if __name__ == '__main__':
    HBNBCommand().cmdloop()
