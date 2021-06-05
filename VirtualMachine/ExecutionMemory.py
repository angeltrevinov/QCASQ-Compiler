from GenerateCode.Function_Dir import Function_Dir
from GenerateCode.Variables_Dir import Variables_Dir
from VirtualMachine.Limits import Limits
import sys

class ExecutionMemory:
    """
    Class that controls the state of the memory during
    execution time.

    :Date: 06-02-2021
    :Version: 1
    :Authors:
        - Angel Treviño A01336559
        - Julia Jimenez A00821428
    """

    base = Limits().offsets  # object that contains the base address for types
    division = Limits().division  # object that contains how many each type gets
    sleeping_memory = []  # to store the accumulated memories if we enter a function
    stack_of_new_memory = []

    # Object that controls current memory
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

    def reserve_global_memory(self, varsNum: dict):
        """
        Method that fills the global memory with the spaces needed
        :param varsNum: The number of variables declared in the global scope
        :type varsNum: dict
        """
        self.memory["global"][self.base["intG"]] = [None] * varsNum["int"]
        self.memory["global"][self.base["floatG"]] = [None] * varsNum["float"]
        self.memory["global"][self.base["stringG"]] = [None] * varsNum["string"]
        self.memory["global"][self.base["boolG"]] = [None] * varsNum["bool"]

    def reserve_cte_memory(self, constants: dict):
        """
        Memory that fills the constant memory with the spaces needed
        for each constant used inside the program
        :param constants: Number of constants for each type
        :type constants: dict
        """
        self.memory["constant"][self.base["intC"]] = [None] * len(constants["int"])
        self.memory["constant"][self.base["floatC"]] = [None] * len(constants["float"])
        self.memory["constant"][self.base["stringC"]] = [None] * len(constants["string"])
        self.memory["constant"][self.base["boolC"]] = [None] * len(constants["bool"])

        self.save_cte_value("intC", constants["int"])
        self.save_cte_value("floatC", constants["float"])
        self.save_cte_value("stringC", constants["string"])
        self.save_cte_value("boolC", constants["bool"])

    def save_cte_value(self, value_type: str, vars: dict):
        """
        Method that stores the constant value in their
        corresponding address in the memory.
        :param value_type: the type of constant to store
        :type value_type: str
        :param vars: The value and address to store it at
        :type vars: dict
        """
        start = self.base[value_type]
        for var in vars:
            offset = vars[var] - start
            self.memory["constant"][start][offset] = self.cast_to_type_cte(value_type, var)

    def cast_to_type_cte(self, value_type: str, var: str):
        """
        Method that casts the data receive, original string,
        to the corresponding type that python can do operations
        with.
        :param value_type: the type to convert to
        :type value_type: str
        :param var: the value
        :type var: str
        :return: the converted value
        """
        value_type = value_type[:len(value_type) - 1]
        if value_type == 'int':
            return int(var)
        elif value_type == 'float':
            return float(var)
        elif value_type == 'bool' and not isinstance(var, int):
            if var == 'false':
                return False
            elif var == 'true':
                return True
            else:
                sys.exit(f"Wrong boolean")
        else:
            return var[1:-1]

    def reserve_local_memory(self, varsNum):
        """
        Method that fills the spaces for the new local memory
        to be used. It does not tell the EM to use it just yet.
        :param varsNum: The number of variables to be created for each type
        :type varsNum: dict
        """
        new_memory_to_be_set = {self.base["intL"]: [None] * varsNum["int"],
                                self.base["floatL"]: [None] * varsNum["float"],
                                self.base["stringL"]: [None] * varsNum["string"],
                                self.base["boolL"]: [None] * varsNum["bool"]}
        self.stack_of_new_memory.append(new_memory_to_be_set)

    def set_new_memory_to_local(self):
        """
        Sets the new memory created to our local memory inside
        the memory in execution
        """
        self.memory["local"] = self.stack_of_new_memory[-1].copy()
        self.stack_of_new_memory.pop()

    def get_local_memory(self):
        """
        Method that returns the current local memory object
        :return: Current local memory object
        :rtype: dict
        """
        return self.memory["local"]

    def save_memory(self, ip: int):
        """
        Saves the current local memory and the instruction pointer,
        so we can add the new local memory to be used.
        :param ip: The current instruction pointer before we enter a func
        :type ip: int
        """
        data = {
            "memory": self.get_local_memory().copy(),
            "ip": ip
        }
        self.sleeping_memory.append(data)

    def print_memory(self):
        """
        Method that prints the whole current memory in used
        """
        print("This are constants")
        print(self.memory["constant"])
        print("This are globals")
        print(self.memory["global"])
        print("This are locals")
        print(self.memory["local"])

    def cast_type(self, value_type: str, var: str):
        """
        Method that transforms the value received in input
        to the corresponding type it should received
        :param value_type: the type to cast to
        :type value_type: str
        :param var: the value to cast
        :type var: str
        :return: the cast value to our language
        :rtype: the type it should be
        """
        try:
            if value_type == 'int':
                return int(var)
            elif value_type == 'float':
                return float(var)
            elif value_type == 'bool' and not isinstance(var, int):
                # just make sure that we accept our language booleans and pythons booleans
                if var == 'false' or var is False:
                    return False
                elif var == 'true' or var is True:
                    return True
                else:
                    sys.exit(f"Wrong boolean")
            else:
                return var
        except ValueError:
            sys.exit(f"Wrong type of variable received")

    def get_value(self, dir: int, tipo: str):
        """
        Method that retrieves the value inside an address
        :param dir: the direction where the value is
        :type dir: int
        :param tipo: the type of variable to retrieve
        :type tipo: str
        :return: The value in that direction
        """
        # if the direction is global
        if type(dir) == str:
            new_dir = dir[1:-1]
            address_to_search = self.get_value(int(new_dir), tipo)
            return self.get_value(address_to_search, tipo)
        elif dir >= 0 * self.division and dir < 4 * self.division:
            offset = dir - self.base[tipo + "G"]  # calculates the position in the array
            offset = self.cast_type("int", offset)
            obtain_var = self.memory["global"][self.base[tipo + "G"]][offset]
        # if the direction is local
        elif dir >= 4 * self.division and dir < 8 * self.division:
            offset = dir - self.base[tipo + "L"]  # calculates the position in the array
            offset = self.cast_type("int", offset)
            obtain_var = self.memory["local"][self.base[tipo + "L"]][offset]
        # if the direction is constant
        elif dir >= 8 * self.division and dir < 12 * self.division:
            offset = dir - self.base[tipo + "C"]  # calculates the position in the array
            obtain_var = self.memory["constant"][self.base[tipo + "C"]][offset]
        # if the var is none, we throw error of trying to do operations with none values
        if obtain_var == None:
            sys.exit(f"Error: trying to do operations with None in {dir}")
        return obtain_var

    def save_value(self, dir: int, tipo: str, value):
        """
        Method that saves a value in the corresponding address
        :param dir: Address where to store the variable
        :type dir: int
        :param tipo: The type of varibale
        :type tipo: str
        :param value: the value to store
        :type value: the ones supported
        """
        if type(dir) == str:
            new_dir = dir[1:-1]
            address_to_search = self.get_value(int(new_dir), tipo)
            dir = address_to_search
        value = self.cast_type(tipo, value)
        # If its a global variable
        if dir >= 0  * self.division and dir < 4 * self.division:
            offset = dir - self.base[tipo + "G"]
            offset = self.cast_type("int", offset)
            self.memory["global"][self.base[tipo + "G"]][offset] = value
        # If its a local variable
        elif dir >= 4 * self.division and dir < 8 * self.division:
            offset = dir - self.base[tipo + "L"]
            offset = self.cast_type("int", offset)
            self.memory["local"][self.base[tipo + "L"]][offset] = value


    def pass_params_to_new(self, dir: int, tipo: str, value):
        """
        Pass the values send by the calllfunc into their corresponding
        memory location in the new memory created
        :param dir: address where to save it
        :type dir: int
        :param tipo: the type of variable
        :type tipo: str
        :param value: the value to pass
        :type value: the basic types the language handles
        """
        value = self.cast_type(tipo, value)
        # Makes sure that we are actually saving it on local
        if dir >= 4 * self.division and dir < 8 * self.division:
            offset = dir - self.base[tipo + "L"]
            self.stack_of_new_memory[-1][self.base[tipo + "L"]][offset] = value

    def restore_previous_memory(self) -> int:
        """
        Method that wakes up the sleeping memory and assigns
        it as our current local memory in execution
        :return: The instruction pointer to return to
        :rtype: int
        """
        previous_memory = self.sleeping_memory[-1]
        self.memory["local"] = previous_memory["memory"]
        self.sleeping_memory.pop()
        return previous_memory["ip"]