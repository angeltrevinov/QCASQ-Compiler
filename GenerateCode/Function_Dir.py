from GenerateCode.Variables_Dir import Variables_Dir

class Function_Dir:

    def __init__(self):
        self.__func_dict__ = {}
        self.__scope_controller = []

    def get_function(self, name_function: str) -> dict:
        return self.__func_dict__[name_function]

    def add_to_dictionary(self, name_function: str, type: str=""):
        # The function is void
        if not type:
            self.__func_dict__[name_function] = {
                "tablevars": Variables_Dir(),  # TODO: add construction
                "type": "void"
            }
        else:
            self.__func_dict__[name_function] = {
                "tablevars": Variables_Dir(),  # TODO: add construction
                "type": type
            }

    def get_dictionary(self) -> dict:
        return self.__func_dict__

    def print_dictionary(self):
        for element in self.__func_dict__:
            print(
                element + ":",
                self.get_function(element),
                "\nTable Vars:"
            )
            self.get_function(element)["tablevars"].print_dictionary()

    def add_to_scope(self, scope: str):
        self.__scope_controller.append(scope)

    def pop_scope(self):
        self.__scope_controller.pop()

    def get_current_scope(self) -> str:
        return self.__scope_controller[-1]

    def get_scope(self) -> dict:
        return self.__scope_controller