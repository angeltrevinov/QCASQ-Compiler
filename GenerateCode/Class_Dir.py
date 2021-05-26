from GenerateCode.Function_Dir import Function_Dir
from GenerateCode.Variables_Dir import Variables_Dir


class Class_Dir:
    """
    Class that manages the class directory, here we maintain
    control of the scope of classes and add them to the
    directory.
    """

    def __init__(self):
        self.__class_dir__ = {}  # Were we are going to save all our classes
        self.__scope_controller = []  # the stack that controls the current scope

    def get_class(self, name_class: str) -> dict:
        """
        Gets the information of a class based on the name
        :param name_class: name of class
        :type name_class: str
        :return: the information of the class
        :rtype: dict
        """
        return self.__class_dir__[name_class]

    def add_to_dictionary(self, name_class: str, herencia: str = ""):
        """
        Adds the class to the dictionary of classes
        :param name_class: the name of the class to add
        :type name_class: str
        :param herencia: if it has any inheritance
        :type herencia: str
        """
        self.__class_dir__[name_class] = {
            "function_dir": Function_Dir(),
            "tablevars": Variables_Dir(),
            "herencia": herencia
        }

    def get_dictionary(self) -> dict:
        """
        :return: Returns the whole dictionary of our classes
        :rtype: dict
        """
        return self.__class_dir__

    def print_dictionary(self):
        """Prints the whole dictionary with the definition of the table vars for each function saved"""
        for element in self.__class_dir__:
            print("#### CLASS ####")
            print(
                element + ":",
                self.get_class(element))
            print("#### CLASS FUNCTIONS ####")
            self.get_class(element)["function_dir"].print_dictionary()
            print("##### CLASS GLOBAL VARIABLES ####")
            self.get_class(element)["tablevars"].print_dictionary()

    def add_to_scope(self, scope: str):
        """Adds the name of the class or program to the top of the scope stack
        :param scope: The name of the current scope to add
        :type scope: str
        """
        self.__scope_controller.append(scope)

    def pop_scope(self):
        """Removes the current scope and returns to the previous scope."""
        self.__scope_controller.pop()

    def get_current_scope(self) -> str:
        """Get the current scope we are in.

        :return: The name of the scope we are at.
        :rtype: str
        """
        return self.__scope_controller[-1]

    def get_scope(self) -> list:
        """Returns the scope stack

        :return: The scope stacks
        :rtype: list
        """
        return self.__scope_controller

    def add_num_vars(self, count: dict):
        """
        Adds the number of variables that the scope used
        :param count: the count object
        :type count: dict
        """
        self.__class_dir__["varsNum"] = count
