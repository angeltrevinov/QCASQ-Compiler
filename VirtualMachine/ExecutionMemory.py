from GenerateCode.Function_Dir import Function_Dir
from GenerateCode.Variables_Dir import Variables_Dir
from VirtualMachine.Limits import Limits
import sys

class ExecutionMemory:
    base = Limits().offsets
    memory = {
        "global": {
            base["intG"]: [],
            base["floatG"]: [],
            base["stringG"]: [],
            base["boolG"]: [],

        },
        "local": {
            base["intL"]: [],
            base["floatL"]: [],
            base["stringL"]: [],
            base["boolL"]: [],
        },
        "constant": {
            base["intC"]: [],
            base["floatC"]: [],
            base["stringC"]: [],
            base["boolC"]: [],
        }
    }

    def reserve_global_memory(self, varsNum : dict):
        self.memory["global"][self.base["intG"]] = [None] * varsNum["int"]
        self.memory["global"][self.base["floatG"]] = [None] * varsNum["float"]
        self.memory["global"][self.base["stringG"]] = [None] * varsNum["string"]
        self.memory["global"][self.base["boolG"]] = [None] * varsNum["bool"]

        #print(self.memory["global"])

    def reserve_cte_memory(self, constants: dict):
        self.memory["constant"][self.base["intC"]] = [None] * len(constants["int"])
        self.memory["constant"][self.base["floatC"]] = [None] * len(constants["float"])
        self.memory["constant"][self.base["stringC"]] = [None] * len(constants["string"])
        self.memory["constant"][self.base["boolC"]] = [None] * len(constants["bool"])

        self.save_cte_value("intC", constants["int"])
        self.save_cte_value("floatC", constants["float"])
        self.save_cte_value("stringC", constants["string"])
        self.save_cte_value("boolC", constants["bool"])

    def save_cte_value(self, value_type: str, vars: dict):
        start = self.base[value_type]
        for var in vars:
            offset = vars[var] - start
            self.memory["constant"][start][offset] = self.cast_to_type_cte(value_type, var)

    def cast_to_type_cte(self, value_type: str, var: str):
        value_type = value_type[:len(value_type) - 1]
        if value_type == 'int':
            return int(var)
        elif value_type == 'float':
            return float(var)
        elif value_type == 'bool':
            if var == 'false':
                return False
            else:
                return True
        else:
            return var[1:-1]

    def reserve_local_memory(self, varsNum):
        self.memory["local"][self.base["intL"]] = [None] * varsNum["int"]
        self.memory["local"][self.base["floatL"]] = [None] * varsNum["float"]
        self.memory["local"][self.base["stringL"]] = [None] * varsNum["string"]
        self.memory["local"][self.base["boolL"]] = [None] * varsNum["bool"]

    def print_memory(self):
        print("This are constants")
        print(self.memory["constant"])
        print("This are globals")
        print(self.memory["global"])
        print("This are locals")
        print(self.memory["local"])

    def cast_type(self, value_type: str, var: str):
        try:
            if value_type == 'int':
                return int(var)
            elif value_type == 'float':
                return float(var)
            else:
                return var
        except ValueError:
            sys.exit(f"Wrong type of variable recived")

    def get_value(self, dir: int, tipo: str):
        if dir >= 0 and dir < 800:
            offset = dir - self.base[tipo + "G"]
            return self.memory["global"][self.base[tipo + "G"]][offset]
        elif dir >= 800 and dir < 1600:
            offset = dir - self.base[tipo + "L"]
            return self.memory["local"][self.base[tipo + "L"]][offset]
        elif dir >= 1600 and dir < 2400:
            offset = dir - self.base[tipo + "C"]
            return self.memory["constant"][self.base[tipo + "C"]][offset]

    def save_value(self, dir: int, tipo: str, value):
        value = self.cast_type(tipo, value) # 'x' will be removed by the function
        if dir >= 0 and dir < 800:
            offset = dir - self.base[tipo + "G"]
            self.memory["global"][self.base[tipo + "G"]][offset] = value
        elif dir >= 800 and dir < 1600:
            offset = dir - self.base[tipo + "L"]
            self.memory["local"][self.base[tipo + "L"]][offset] = value