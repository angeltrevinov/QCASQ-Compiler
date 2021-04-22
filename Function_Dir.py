from Variables_Dir import *

class Function_Dir:

    __dict__ = {}

    def get_function(self, name_function: str) -> dict:
        return self.__dict__[name_function]

    def add_to_dictionary(self, name_function: str, type: str=""):

        # Constructor of Table variables
        tablevars = Variables_Dir()

        # The function is void
        if not type:
            self.__dict__[name_function] = {
                "tablevars": tablevars,  # TODO: add construction
                "type": "void"
            }
        else:
            self.__dict__[name_function] = {
                "tablevars": tablevars,  # TODO: add construction
                "type": type
            }

    def get_Dictionary(self):
        for element in self.__dict__:
            print(element + ":", self.get_function(element))