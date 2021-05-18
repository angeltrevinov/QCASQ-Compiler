from GenerateCode.Function_Dir import Function_Dir
from GenerateCode.Variables_Dir import Variables_Dir

class Class_Dir:

    def __init__(self):
        self.__class_dir__ = {}
        self.__scope_controller = []  # the stack that controls the current scope


    def get_class(self, name_class: str) -> dict:
        return self.__class_dir__[name_class]

    def add_to_dictionary(self, name_class: str, herencia: str= ""):
        self.__class_dir__[name_class] = {
            "function_dir": Function_Dir(),
            "tablevars": Variables_Dir(),
            "herencia": herencia
        }

    def get_dictionary(self) -> dict:
        return self.__class_dir__

    def print_dictionary(self):
        """Prints the whole dictionary with the definition of the table vars for each function saved"""
        for element in self.__class_dir___:
            print(
                element + ":",
                self.get_function(element),
                "\nTable Vars:"
            )
            self.get_function(element)["tablevars"].print_dictionary()


    def add_to_scope(self, scope: str):
        """Adds the name of the func, class or program to the top of the scope stack
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