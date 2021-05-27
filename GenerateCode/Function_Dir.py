from GenerateCode.Variables_Dir import Variables_Dir


class Function_Dir:

    def __init__(self):
        self.__func_dict__ = {}  # the object that stores all functions
        self.__scope_controller = []  # the stack that controls the current scope

    def get_function(self, name_function: str) -> dict:
        """Get the function object

        :param name_function: The name of the function to retrieve
        :type name_function: str
        :return: The function dictionary
        :rtype: dict
        """
        return self.__func_dict__[name_function]

    def add_to_dictionary(self, name_function: str, type: str="void"):
        """Adds a function to the current dictionary

        :param name_function: the name of the function to add
        :type name_function: str
        :param type: The type of the function to add (if not included, its going to be void)
        :type type: str
        """
        self.__func_dict__[name_function] = {
            "tablevars": Variables_Dir(),
            "params": Variables_Dir(),
            "type": type,
        }

    def get_dictionary(self) -> dict:
        """Gets the whole function dictionary

        :return: The functions dictionary
        :rtype: dict
        """
        return self.__func_dict__

    def print_dictionary(self):
        """Prints the whole dictionary with the definition of the table vars for each function saved"""
        for element in self.__func_dict__:
            print(
                element + ":",
                self.get_function(element),
                "\nTable Vars:"
            )
            self.get_function(element)["tablevars"].print_dictionary()
            self.get_function(element)["params"].print_dictionary()

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

    def add_num_vars(self, count : dict, name_function: str):
        self.__func_dict__[name_function]["varsNum"] = count

    def add_quad_dir(self, dir: int, name_function: str):
        self.__func_dict__[name_function]["startQuad"] = dir