
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
        "boolC": 2200,
        ## Temporales
        "intT": 2400,
        "floatT": 2600,
        "stringT": 2800,
        "boolT": 3000
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
        "boolC": 0,
        ## Temporales
        "intT": 0,
        "floatT": 0,
        "stringT": 0,
        "boolT": 0
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
        ints = self.cont["intL"] + self.cont["intT"]
        floats = self.cont["floatL"] + self.cont["floatT"]
        string = self.cont["stringL"] + self.cont["stringT"]
        bool = self.cont["boolL"] + self.cont["boolT"]

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
        self.cont["intT"] = 0
        self.cont["floatT"] = 0
        self.cont["stringT"] = 0
        self.cont["boolT"] = 0

