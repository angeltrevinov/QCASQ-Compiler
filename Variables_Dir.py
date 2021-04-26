
class Variables_Dir:

    def __init__(self):
        self.__func_dict__ = {}

    def get_variable(self, name_var: str) -> dict:
        return self.__func_dict__[name_var]

    def add_to_dictionary(self, name_var: str, type: str):
        # The function is void
        self.__func_dict__[name_var] = {
            "type": type,
            "value": None
        }

    def get_dictionary(self) -> dict:
        return self.__func_dict__

    def print_dictionary(self):
        for element in self.__func_dict__:
            print("\t" + element + ":", self.get_variable(element))