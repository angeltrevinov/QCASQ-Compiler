
# TODO: Add to memory class divisions
'''
    Structure to use = Dict
'''
class Memory:
    offsets =  {
        ## Globales
        "intG" : 0,
        "intGT" : 200,
        "floatG" : 400,
        "floatGT" : 600,
        "stringG" : 800,
        "stringGT": 1000,
        "boolG" : 1200,
        "boolGT": 1400,
        ## Locales
        "intL": 1600,
        "intLT": 1800,
        "floatL": 2000,
        "floatLT": 2200,
        "stringL": 2400,
        "stringLT": 2600,
        "boolL": 2800,
        "boolLT": 3000,
        ## Constantes
        "intC": 3200,
        "floatC": 3400,
        "stringC": 3600,
        "boolC": 3800
    }

    cont = {
        ## Globales
        "intG": 0,
        "intGT": 0,
        "floatG": 0,
        "floatGT": 0,
        "stringG": 0,
        "stringGT": 0,
        "boolG": 0,
        "boolGT": 0,
        ## Locales
        "intL": 0,
        "intLT": 0,
        "floatL": 0,
        "floatLT": 0,
        "stringL": 0,
        "stringLT": 0,
        "boolL": 0,
        "boolLT": 0,
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