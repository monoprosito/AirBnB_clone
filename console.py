#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Console Module
This module controls all databases.
Can create, modify and delete instances.
"""


from datetime import datetime
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command processor class."""
    prompt = '(hbnb) '
    allowed_classes = ['BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review']

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel.
        """
        command = self.parseline(line)[0]
        if command is None:
            print('** class name missing **')
        elif command not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(command)()
            new_obj.save()
            print(new_obj.id)

    def emptyline(self):
        """Emptyline Documentation
        Method called when an empty line is entered in
        response to the prompt. If this method is not
        overridden, it repeats the last nonempty
        command entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
