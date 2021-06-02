import sys

# TODO: Add to memory class divisions


class Limits:
    """
    Class that controls the limits and divisions for the scopes
    and the types of variables for those scopes.

    :Date: 06-02-2021
    :Version: 1
    :Authors:
        - Angel Treviño A01336559
        - Julia Jimenez A00821428
    """

    division = 200  # The number of spaces each type gets

    # Store the divisions for each scope and type
    offsets = {
        # Globales
        "intG" : 0 * division,
        "floatG" : 1 * division,
        "stringG" : 2 * division,
        "boolG" : 3 * division,
        # Locales
        "intL": 4 * division,
        "floatL": 5 * division,
        "stringL": 6 * division,
        "boolL": 7 * division,
        # Constantes
        "intC": 8 * division,
        "floatC": 9 * division,
        "stringC": 10 * division,
        "boolC": 11 * division
    }
    # Object that keeps track of how many variables we have created for each type
    cont = {
        # Globales
        "intG": 0,
        "floatG": 0,
        "stringG": 0,
        "boolG": 0,
        # Locales
        "intL": 0,
        "floatL": 0,
        "stringL": 0,
        "boolL": 0,
        # Constantes
        "intC": 0,
        "floatC": 0,
        "stringC": 0,
        "boolC": 0
    }

    def getAddress(self, type: str) -> int:
        """
        Method that gets the new address to use
        :param type: the type of variable
        :type type: str
        :return: the new address to use
        :rtype: int
        """
        return self.offsets[type]

    def upCont(self, type: str, add: int = 1):
        """
        Method that updates how many variables we have used
        for that type.
        :param type: the type of variable
        :type type: str
        :param add: How many to add, if not included, its 1
        :type add: int
        """
        self.cont[type] = self.cont[type] + add

    def getCont(self, type: str) -> int:
        """
        Get the current counter for the corresponding type
        :param type: the type of variable
        :type type: str
        :return: How many we have added
        :rtype: int
        """
        return self.cont[type]

    def check_limits(self, address: int, tipo: str):
        """
        Method that checks that the address is not outside their
        corresponding limits
        :param address: the address to check
        :type address: int
        :param tipo: the type of varibale
        :type tipo: str
        """
        in_limits = False
        if address >= self.offsets[tipo] and address < self.offsets[tipo] + self.division:
            in_limits = True
        if in_limits == False:
            sys.exit(f"ERROR: Too many variables")

    def get_global_vars_count(self) -> dict:
        """
        Returns the global variables count
        :return: how many variables we have for each type
        :rtype: dict
        """
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

    def get_local_vars_count(self) -> dict:
        """
        Returns the local variables count
        :return: how many variables we have for each count
        :rtype: dict
        """
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
        """
        Method that resets the count for locals to 0 when
        we enter a new function
        """
        self.cont["intL"] = 0
        self.cont["floatL"] = 0
        self.cont["stringL"] = 0
        self.cont["boolL"] = 0

