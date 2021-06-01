import sys
# TODO: Add to memory class divisions
'''
    Structure to use = Dict
'''
class Limits:
    division = 200
    offsets =  {
        ## Globales
        "intG" : 0 * division,
        "floatG" : 1 * division,
        "stringG" : 2 * division,
        "boolG" : 3 * division,
        ## Locales
        "intL": 4 * division,
        "floatL": 5 * division,
        "stringL": 6 * division,
        "boolL": 7 * division,
        ## Constantes
        "intC": 8 * division,
        "floatC": 9 * division,
        "stringC": 10 * division,
        "boolC": 11 * division
    }

    cont = {
        ## Globales
        "intG": 0,
        "floatG": 0,
        "stringG": 0,
        "boolG": 0,
        ## Locales
        "intL": 0,
        "floatL": 0,
        "stringL": 0,
        "boolL": 0,
        ## Constantes
        "intC": 0,
        "floatC": 0,
        "stringC": 0,
        "boolC": 0
    }

    def getAddress(self, type: str):
        return self.offsets[type]

    def upCont(self, type: str, add: int=1):
        self.cont[type] = self.cont[type] + add

    def getCont(self, type: str):
        return self.cont[type]

    def check_limits(self, address:int, tipo: str):
        print(address, tipo)
        in_limits = False
        if address >= self.offsets[tipo] and address < self.offsets[tipo] + self.division:
            in_limits = True

        if in_limits == False:
            sys.exit(f"ERROR: Too many variables")

    def get_global_vars_count(self):
        ints = self.cont["intG"]
        floats = self.cont["floatG"]
        string = self.cont["stringG"]
        bool = self.cont["boolG"]

        obj = {
            "int" : ints,
            "float" : floats,
            "string" : string,
            "bool" : bool
        }
        return obj

    def get_local_vars_count(self):
        ints = self.cont["intL"]
        floats = self.cont["floatL"]
        string = self.cont["stringL"]
        bool = self.cont["boolL"]

        obj = {
            "int": ints,
            "float": floats,
            "string": string,
            "bool": bool
        }
        return obj

    def reset_locals(self):
        self.cont["intL"] = 0
        self.cont["floatL"] = 0
        self.cont["stringL"] = 0
        self.cont["boolL"] = 0

