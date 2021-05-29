from VirtualMachine.Limits import Limits
class CteTable:
    """
    Class that manages our constants used and reserves a
    space in our memory.
    """
    division = Limits().division
    ints = {}
    floats = {}
    strings = {}
    # Set them right now because we only had two.
    bools = {
        "true" : 11 * division,
        "false" : 11 * division + 1
    }

    def addInt(self, value: str, address: int) -> bool:
        """Method that adds the constant int to the table

        :param value: constant to add
        :type value: str
        :param address: address to store at
        :type address:int
        :return: If it could added
        :rtype: bool
        """
        if value not in self.ints:
            self.ints[value] = address
            return True
        else:
            return False

    def getInt(self, value: str):
        return self.ints[value]

    def addFloat(self, value: str, address: int):
        if value not in self.floats:
            self.floats[value] = address
            return True

    def getFloat(self, value: str):
        return self.floats[value]

    def addString(self, value: str, address: int):
        if value not in self.strings:
            self.strings[value] = address
            return True

    def getString(self, value: str):
        return self.strings[value]

    def addBool(self, value: str, address: int):
        if value not in self.bools:
            self.bools[value] = address
            return True

    def getBool(self, value: str):
        return self.bools[value]

    def get_ctes_table(self):
        obj = {
            "int" : self.ints,
            "float" : self.floats,
            "string" : self.strings,
            "bool" : self.bools
        }

        return obj

    def print_ctes(self):
        print("Aqui empiezan los INT")
        self.print_tipo(self.ints)
        print("Aqui empiezan los FLOAT")
        self.print_tipo(self.floats)
        print("Aqui empiezan los STRING")
        self.print_tipo(self.strings)
        print("Aqui empiezan los BOOL")
        self.print_tipo(self.bools)

    def print_tipo(self, dicc:dict):
        for element in dicc:
            print(element, dicc[element])