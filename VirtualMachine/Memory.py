from GenerateCode.Class_Dir import Class_Dir
# TODO: Add to memory class divisions
'''
    //// 0 - 999
    int globals -> 0 249
    float globals -> 250 - 499
    string globals -> 500 - 749
    bool globals -> 750 - 999

    //// 1000 - 1999
    int local -> 1000 - 1249
    float local -> 1250 - 1499
    string local -> 1500 - 1749
    bool local -> 1750 - 1999

    //// 2000 - 2999
    int temp -> 2000 - 2249
    float temp -> 2250 - 2499
    string temp -> 2500 - 2749
    bool temp -> 2750 - 2999

    Structure to use = Dict
'''
class Memory:
    offsets =  {
        "intG" : 0,
        "floatG" : 250,
        "stringG" : 500,
        "boolG" : 750,
        "intL": 1000,
        "floatL": 1250,
        "stringL": 1500,
        "boolL": 1750,
        "intT": 2000,
        "floatT": 2250,
        "stringT": 2500,
        "boolT": 2750,
    }

    def __init__(self):
        self.__memory__ = {
            # key(numero) : value
        }

    def save_global_vars(self, directory: Class_Dir, scope: str = "G"):
        for index, element in enumerate(directory.get_dictionary()):
            if index == 0:
                self.get_vars(directory, element, scope)
                return


    def get_vars(self, directory: Class_Dir, element: str, scope: str):
        conts = {
            "int": 0,
            "float": 0,
            "string": 0,
            "bool": 0
        }
        vars = directory.get_class(element)["tablevars"].get_dictionary()
        for var in vars:
            tipo = vars[var]["type"]
            self.__memory__[conts[tipo] + self.offsets[tipo + scope]] = None
            conts[tipo] = conts[tipo] + 1


    def print_memory(self):
        dictionary_items = self.__memory__.items()
        sorted_items = sorted(dictionary_items)
        for element in sorted_items:
            print(element)
