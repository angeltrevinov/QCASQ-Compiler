
class Variables_Dir:

    def __init__(self):
        self.__var_dict__ = {}  # the var directory object

    def get_variable(self, name_var: str) -> dict:
        """Gets a variable from the current var directory based on the specified name.

        :param name_var: Name of the variable to retrieve
        :type name_var: str
        :return: The var object, with its type and value
        :rtype: dict
        """
        return self.__var_dict__[name_var]

    def add_to_dictionary(self, name_var: str, type: str, cont: int):
        """ Adds the incoming variable with its type to the variable directory.

        :param name_var: Name of the variable
        :type name_var: str
        :param type: The type of the variable
        :type type: str
        """
        self.__var_dict__[name_var] = {
            "type": type,
            "address": cont
        }

#TODO:
# Crear tabla de constantes globales
# Clases definir divisiones con sus divisiones de global y local
    def get_dictionary(self) -> dict:
        """Returns the variable dictionary object

        :return: The variable dictionary
        :rtype: dict
        """
        return self.__var_dict__

    def print_dictionary(self):
        """Prints the contents of the variable dictionary object"""
        for element in self.__var_dict__:
            print("\t" + element + ":", self.get_variable(element))