
class Variables_Dir:

    __dict__ = {}

    def get_variable(self, name_var: str) -> dict:
        return self.__dict__[name_var]

    def add_to_dictionary(self, name_var: str, type: str):
        # The function is void
        self.__dict__[name_var] = {
            "type": type,
            "value": None
        }

    def get_Dictionary(self):
        for element in self.__dict__:
            print(element + ":", self.get_variable(element))