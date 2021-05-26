
class CteTable:
    ints = {}
    floats = {}
    strings = {}
    bools = {
        "true" : 2200,
        "false" : 2201
    }

    def addInt(self, value: str, address: int):
        if value not in self.ints:
            self.ints[value] = address

    def getInt(self, value: str):
        return self.ints[value]

    def addFloat(self, value: str, address: int):
        if value not in self.floats:
            self.floats[value] = address

    def getFloat(self, value: str):
        return self.floats[value]

    def addString(self, value: str, address: int):
        if value not in self.strings:
            self.strings[value] = address

    def getString(self, value: str):
        return self.strings[value]

    def addBool(self, value: str, address: int):
        if value not in self.bools:
            self.bools[value] = address

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