
# TODO: Add to memory class divisions
'''
    Structure to use = Dict
'''
class Limits:
    offsets =  {
        ## Globales
        "intG" : 0,
        "floatG" : 200,
        "stringG" : 400,
        "boolG" : 600,
        ## Locales
        "intL": 800,
        "floatL": 1000,
        "stringL": 1200,
        "boolL": 1400,
        ## Constantes
        "intC": 1600,
        "floatC": 1800,
        "stringC": 2000,
        "boolC": 2200
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

    def upCont(self, type: str):
        self.cont[type] = self.cont[type] + 1

    def getCont(self, type: str):
        return self.cont[type]

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

