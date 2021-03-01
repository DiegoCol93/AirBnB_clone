#!/usr/bin/python3
"""
.______________________________________________________________.
|                                                              |
|    Command Line Interpreter source code for managing the     |
|      serialization and deserialization, attributes and       |
|  methods of the object classes present in the AirBnB clone.  |
|                                                              |
|\033[92m   _____     __    ______    ______    ______      __         \033[0m|
|\033[92m  /\  __-.  /\ \  /\  ___\  /\  ___\  /\  __ \    /\ \        \033[0m|
|\033[92m  \ \ \/\ \ \ \ \ \ \  __\  \ \ \__ \ \ \ \/\ \   \ \ \____   \033[0m|
|\033[92m   \ \____-  \ \_\ \ \_____\ \ \_____\ \ \_____\   \ \_____\  \033[0m|
|\033[92m    \/____/   \/_/  \/_____/  \/_____/  \/_____/    \/_____/  \033[0m|
|\033[92m         __   __    __    ______    ______      ______        \033[0m|
|\033[92m        /\ '-.\ \  /\ \  /\  ___\  /\  __ \    /\  ___\       \033[0m|
|\033[92m        \ \ \-.  \ \ \ \ \ \ \____ \ \ \/\ \   \ \___  \      \033[0m|
|\033[92m         \ \_\ '\_\ \ \_\ \ \_____\ \ \_____\   \/\_____\     \033[0m|
|\033[92m          \/_/ \/_/  \/_/  \/_____/  \/_____/    \/_____/     \033[0m|
|                                                              |
|                         Feb - 2021                           |
|______________________________________________________________|\n
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User
from models import storage
import cmd

# List of currently implemented classes.
list_of_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                   "Review"]

# List of currently available methods.
list_of_methods = ["create", "show", "destroy", "all", "update", "count"]


class HBNBCommand(cmd.Cmd):
    """
    Command line interpreter class for handling the main loop and
    interact with the available classes.\n"""

    prompt = "(hbnb) "  # <--- Defines the look of the prompt.

    # precmd- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def precmd(self, line):
        """ Method for parsing ClassName.method() imput strings. """

        # Setup switch for testing if found the correct strings.
        switch = False
        # If line exists.
        if line:

            # If line ends with the ")" character.
            if line.endswith(")"):

                # Check for number of ")" characters
                number = line.count(")")
                if number != 1:
                    return line

                # Split to get string behind ")".
                split_close_parenthesis = line.split(")")

                # Check for number of "(" characters
                number = split_close_parenthesis[0].count("(")
                if number != 1:
                    return line

                # Split to get string behind "(".
                split_open_parenthesis = split_close_parenthesis[0].split("(")

                # If arguments were given whitin the parenthesis.
                args = ""
                if len(split_open_parenthesis) > 1:
                    args = split_open_parenthesis[1]

                # Split to get strings before and after ".".
                split_dot = split_open_parenthesis[0].split(".")

                # Compare "ClassName". with list_of_classes.
                for name in list_of_classes:
                    # If found the correct ClassName.
                    if split_dot[0] == name:
                        switch = True
                        # Compare ."method" with list_of_methods.
                        for method in list_of_methods:
                            switch = False
                            # If found the correct method name.
                            if split_dot[1] == method:
                                switch = True
                                # Concat the string.
                                command = "{} {} {}".format(split_dot[1],
                                                            split_dot[0],
                                                            args)
                                # Return the formatted command.
                                return(command)

        # If not found correct ClassName.method(<args>) combinations.
        if switch is False:
            return(line)

    # emptyline - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def emptyline(self):
        """ Handles the event when entering an empty line. """
        pass

    # Implementations 1.0 ----------------------------------------------------|
    # do_create - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_create(self, line):
        """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Creates a new Class instance.\n""" \
            """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Currently available classes:\n""" \
            """  \033[92m|\033[0m\n""" \
            """\033[92m""" \
            """  |      BaseModel     User        State\n""" \
            """  |      City          Amenity     Place\n""" \
            """  |      Review\n""" \
            """  \033[92m|\033[0m\n""" \
            """\033[0m""" \
            """  \033[92m| -\033[0m Usage:\n""" \
            """  \033[92m|\033[0m\n""" \
            """  \033[92m|\033[0m        """ \
            """create <\033[92mclass name\033[0m>\n""" \
            """  \033[92m|\033[0m"""

        """ ---------- Method for creating a new class instance. ---------- """

        # If line exists.
        if line:

            # Set up switch
            switch = False

            # Compare given class name against list of classes.
            for name in list_of_classes:

                # If found correct ClassName.
                if line == name:
                    x = eval(name)()  # <--Create instance.
                    storage.new(x)  # <-- Store instance
                    storage.save()  # <-- Save changes onto file.
                    print(x.id)  # <-- Print id of created instance.
                    switch = True  # <-- Set switch
                    break

            # If couldn't find a correct ClassName
            if switch is False:
                print("** class doesn't exist **")

        # If line empty
        else:
            print("** class name missing **")

    # do_show - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_show(self, line):
        """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Shows an active class instance given i""" \
            """ts class name and id.\n""" \
            """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Usage:\n""" \
            """  \033[92m|\033[0m\n""" \
            """  \033[92m|\033[0m        """ \
            """show <\033[92mclass name\033[0m> <\033[92mid\033[0m>\n""" \
            """  \033[92m|\033[0m"""

        """ ------ Method for showing an specific object by its id. ------ """

        # If line exists.
        if line:
            # Slipt arguments.
            args = line.split(" ")
            # Compare switch.
            switch = False

            # Compare given class name against list of classes.
            for name in list_of_classes:
                if args[0] == name:
                    switch = True
                    break

            # If found the correct class name
            if switch is True:
                # If given an id
                if len(args) > 1:
                    # Remove the " on the id string.
                    args[1] = args[1].strip('"')
                    # Create ClassName.id string
                    string = args[0] + "." + args[1]
                    # Reload all objects from file.
                    storage.reload()
                    # Retrieve dictionary of objects
                    dicto = storage.all()

                    switch = False  # <-- Set switch for looking in dictionary.

                    # Run through dictionary
                    for obj_id, obj in dicto.items():
                        # If correct ClassName.id found.
                        if string == obj_id:
                            print(obj)
                            switch = True
                    if switch is False:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    # do_destroy - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
    def do_destroy(self, line):
        """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Deletes an instance of a class given i""" \
            """ts id.\n""" \
            """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Usage:\n""" \
            """  \033[92m|\033[0m\n""" \
            """  \033[92m|\033[0m        """ \
            """destroy <\033[92mclass name\033[0m> <\033[92mid\033[0m>\n""" \
            """  \033[92m|\033[0m"""

        """ -------- Method for destroying an object using its id. -------- """

        # If line exists.
        if line:
            # Split in arguments.
            args = line.split(" ")
            # Compare switch.
            switch = False

            # Compare given class name against list of classes.
            for name in list_of_classes:
                if args[0] == name:
                    switch = True
                    break

            # If correct ClassName found.
            if switch is True:
                # If id was given.
                if len(args) > 1:
                    # Remove the " on the id string.
                    args[1] = args[1].strip('"')
                    # If found an instance to delete.
                    if storage.delete(args[0], args[1]) is False:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    # do_all - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
    def do_all(self, line):
        """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Prints all the objects currently pre""" \
            """sent or if the class name is given,\n""" \
            """  \033[92m|\033[0m""" \
            """       all objects of the same class.\n""" \
            """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Usage:\n""" \
            """  \033[92m|\033[0m\n""" \
            """  \033[92m|\033[0m""" \
            """        all\n""" \
            """  \033[92m|\033[0m""" \
            """        all <\033[92mclass name\033[0m>\n""" \
            """  \033[92m|\033[0m""" \
            """        <\033[92mclass name\033[0m>.all()\n""" \
            """  \033[92m|\033[0m"""

        """ ------------ Method for printing all the objects. ------------ """

        # Reload all instances from the .json file.
        storage.reload()
        # Get the dictionary of objects.
        dicto = storage.all()
        # Create empty list for printing.
        list_of_strings = []

        # If only all command was given.
        if line == "":

            # For all objects in the dict append their str representation.
            for obj_id, obj in dicto.items():
                list_of_strings.append(obj.__str__())

            # If list_of_strings is not empty.
            if bool(list_of_strings):
                print(list_of_strings)

        # Else if the class name was given.
        else:
            # Compare switch.
            switch = False
            args = line.split(" ")

            # If number of arguments given is correct.
            if len(args) == 1 and args[0].isalpha():

                # Compare given class name against list of classes.
                for name in list_of_classes:
                    if args[0] == name:
                        switch = True
                        break

                # If found the correct class name.
                if switch is True:

                    # Append only the string rep. of the given objects.
                    for obj_id, obj in dicto.items():
                        # Split the ClassName.id key.
                        class_name = obj_id.split(".")
                        # If the class name is correct.
                        if args[0] == class_name[0]:
                            # Append the string rep of the object.
                            list_of_strings.append(obj.__str__())

                # If list_of_strings is not empty.
                if bool(list_of_strings):
                    print(list_of_strings)

                # If no class name found.
                if switch is False:
                    print("** class doesn't exist **")

    # do_update - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_update(self, line):
        """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Updates or adds an attribute of a Clas""" \
            """s instance given its name, id, the\n""" \
            """  \033[92m|\033[0m""" \
            """    attribute to add and the value for it, only one attr""" \
            """ibute can be set up\n""" \
            """  \033[92m|\033[0m""" \
            """    at a time using the command but a dictionary may be """ \
            """give to update\n""" \
            """  \033[92m|\033[0m""" \
            """    several attributes.\n""" \
            """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Usage:\n""" \
            """  \033[92m|\033[0m\n""" \
            """  \033[92m|        \033[0m""" \
            """update <\033[92mclass name\033[0m> <\033[92mid\033[0m> """ \
            """<\033[92mattribute name\033[0m> \033[92m"\033[0m<\033[92mat""" \
            '''tribute value\033[0m>\033[92m"\033[0m\n''' \
            """  \033[92m|\033[0m"""

        """ --------------- Method for updating an object. --------------- """

        # If line exists.
        while line:
            # Change single ' to double " for cmds running non-tty.
            line = line.replace("'", '"')

            # If dictionary was given.
            if line.endswith('}'):
                # Set up empty list for iteration.
                list_of_key_value = []
                # Split ClassName.update from , {key:value}
                args = line.split(" ", 2)
                # Remove , character from id
                args[1] = args[1].strip(",")
                # Remove " characters from id
                args[1] = args[1].strip('"')

                # Split dictionary
                list_of_key_value = args[2].split(", ")

                for pair in list_of_key_value:
                    pairs = pair.strip("{")
                    pairs = pairs.strip("}")
                    pairs = pairs.split(": ")
                    key = pairs[0].strip('"')
                    value = pairs[1]
                    command = args[0] + " " + args[1] + " " + key + " " + value
                    self.do_update(command)
                break

            elif line.endswith('"'):
                arg = line.split(" ")
                # Remove the , characters
                arg[0] = arg[0].strip(",")
                arg[1] = arg[1].strip(",")
                arg[2] = arg[2].strip(",")
                # Remove the " characters
                arg[0] = arg[0].strip('"')
                arg[1] = arg[1].strip('"')
                arg[2] = arg[2].strip('"')
                line = arg[0] + " " + arg[1] + " " + arg[2] + " " + arg[3]

            elif line[-1].isdigit():
                arg = line.split(" ")
                # Remove the , characters
                arg[0] = arg[0].strip(",")
                if len(arg) > 1:
                    arg[1] = arg[1].strip(",")
                if len(arg) > 2:
                    arg[2] = arg[2].strip(",")
                # Remove the " characters
                arg[0] = arg[0].strip('"')
                if len(arg) > 1:
                    arg[1] = arg[1].strip('"')
                if len(arg) > 2:
                    arg[2] = arg[2].strip('"')
                if len(arg) > 3:
                    ending = '{}"'.format(arg[3])
                    line = arg[0] + " " + arg[1] + " " + arg[2] + ' "' + ending

            if line.count("{"):
                line = None

            # Split once delimited by " character.
            val = line.split('"')

            # Split normally a second time the first arguments.
            arg = val[0].split(" ")

            # Compare switch
            switch = False

            # Compare given class name against list of classes.
            for name in list_of_classes:
                if arg[0] == name:
                    switch = True
                    break

            # If correct class name given.
            if switch is True:
                # If given an id.
                if len(arg) > 1:
                    obj_id = arg[0] + "." + arg[1]  # <--- ClassName.id string.
                    # If name of attribute given.
                    if len(arg) > 2:
                        # If value for the attribute was given.
                        if len(val) > 1:
                            # If the given value is a digits only string.
                            if val[1].isdigit():
                                # Cast it to int.
                                val[1] = int(val[1])

                            # If there's a . character
                            elif val[1].count(".") == 1:
                                if val[1].replace(".", "").isdigit():
                                    val[1] = float(val[1])

                            # If no instance exists by the given.
                            if storage.update(obj_id, arg[2], val[1]) is False:
                                print("** no instance found **")
                                break
                            else:
                                break
                        else:
                            print("** value missing **")
                            break
                    else:
                        print("** attribute name missing **")
                        break
                else:
                    print("** instance id missing **")
                    break
            else:
                print("** class doesn't exist **")
                break
        else:
            print("** class name missing **")

    # do_count- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_count(self, line):
        """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Counts and prints the number of instan""" \
            """ces with the given ClassName\n""" \
            """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Usage:\n""" \
            """  \033[92m|\033[0m\n""" \
            """  \033[92m|\033[0m""" \
            """        <\033[92mclass name\033[0m>.count()\n""" \
            """  \033[92m|\033[0m"""

        """ Counts and prints the number of instances """

        # Split to chek no extra arguments were given.
        args = line.split(" ")

        # If only one argument was passed.
        if len(args) == 1:
            # Load latest changes.
            storage.reload()
            # Retrieve dictionary of objects
            dicto = storage.all()

            # number to store times an instance appears on dicto
            number = 0

            # Setup switch
            switch = False

            # Compare agaist ClassName.id keys.
            for obj_id, obj in dicto.items():
                # Split the ClassName.id key.
                class_name = obj_id.split(".")
                # If the class name is correct.
                if args[0] == class_name[0]:
                    switch = True
                    number += 1

                # Compare given class name against list of classes.
                for name in list_of_classes:
                    if args[0] == name:
                        switch = True
                        break

            # If found the correct class name
            if switch is True:
                print(number)
            # else:
            #     print("** class doesn't exist **")
        else:
            pass

    # Implementations 0.0.1---------------------------------------------------|
    # do_quit - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_quit(self, line):
        """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Exits the program.\n""" \
            """  \033[92m|\033[0m"""
        print("")
        return True

    # do_EOF - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
    def do_EOF(self, line):
        """  \033[92m|\033[0m\n""" \
            """  \033[92m| -\033[0m Exits the program.\n""" \
            """  \033[92m|\033[0m"""
        print("")
        return True

# If being executed not imported - - - - - - - - - - - - - - - - - - - - - - -|
if __name__ == '__main__':
    '''name main'''
    green = "\033[92m"  # <-- Green color format
    red = "\033[91m"  # <-- Red color format
    reset = "\033[0m"  # <-- Default color format

    # Green help string
    hlp = green + "help" + reset

    # Green quit string
    qut = green + "quit" + reset

    # Green title message
    title_string = green + "Welcome to the hbnb C.L.I" + reset

    # Regular intro.
    intro_string = "._______________________________.\n" \
                   "|                               |\n" \
                   "|   " + title_string + "   |\n" \
                   "|                               |\n" \
                   "|     for help, type '" + hlp + "'     |\n" \
                   "|      to quit, type '" + qut + "'     |\n" \
                   "|_______________________________|\n"

    # Pretty intro.
    air = "._____________________________________________________.\n" \
          "|                                                     |\n" \
          "|             \033[92m\033[4m " \
          "Welcome to the hbnb C.L.I \033[0m             |\n" \
          "|\033[92m\033[5m" \
          "    ______  __  ______  ______  __   __  ______" \
          "\033[0m      |\n" \
          "|\033[92m\033[5m" \
          "   /\  __ \/\ \/\  == \/\  == \/\ \"-.\ \/\  == \ " \
          "\033[0m    |\n" \
          "|\033[92m\033[5m" \
          "   \ \  __ \ \ \ \  __<\ \  __<\ \ \-.  \ \  __<" \
          "\033[0m     |\n" \
          "|\033[92m\033[5m" \
          "    \ \_\ \_\ \_\ \_\ \_\ \_____\ \_\\\\\"\_\ \_____\ " \
          "\033[0m  |\n" \
          "|\033[92m\033[5m" \
          "     \/_/\/_/\/_/\/_/ /_/\/_____/\/_/ \/_/\/_____/" \
          "\033[0m   |\n" \
          "|                                                     |\n" \
          "|                for help, type '" + hlp + "'                " \
          "|\n|                 to quit, type '" + qut + "'             " \
          "   |\n|\033[92m" \
          "        Written by Diego Lopez & Nicolas Soler.\033[0m      |\n" \
          "|_____________________________________________________|\n"

    # Start running the cmd loop
    HBNBCommand().cmdloop(air)
