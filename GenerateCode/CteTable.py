from VirtualMachine.Limits import Limits


class CteTable:
    """
    Class that manages our constants used and reserves a
    space in our memory.

    :Date: 06-02-2021
    :Version: 1
    :Authors:
    - Angel Treviño A01336559
    - Julia Jimenez A00821428
    """

    division = Limits().division  # import the division for each type
    ints = {}
    floats = {}
    strings = {}
    # Only two constants for floats, not big deal if we add them now
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

    def getInt(self, value: str) -> int:
        """
        Method that returns the address of a corresponding int
        constant
        :param value: value to get address
        :type value: str
        :return: the address of the constant
        :rtype: int
        """
        return self.ints[value]

    def addFloat(self, value: str, address: int) -> bool:
        """
        Method that adds the float value and its address
        :param value: the float value
        :type value: str
        :param address: the corresponding address
        :type address: int
        :return: if it can added or not
        :rtype: bool
        """
        if value not in self.floats:
            self.floats[value] = address
            return True
        else:
            return False

    def getFloat(self, value: str) -> int:
        """
        Method that gets the address of the corresponding float value
        :param value: float constant to get address
        :type value: str
        :return: The address of the constant value
        :rtype: int
        """
        return self.floats[value]

    def addString(self, value: str, address: int) -> bool:
        """
        Method that adds the String value and its address
        :param value: string constant
        :type value: str
        :param address: address where is at
        :type address: int
        :return: If it could be added or not
        :rtype: bool
        """
        if value not in self.strings:
            self.strings[value] = address
            return True
        else:
            return False

    def getString(self, value: str) -> int:
        """
        Method that gets the address of the corresponding string constant
        :param value: the string constant
        :type value: str
        :return: the address
        :rtype: int
        """
        return self.strings[value]

    def addBool(self, value: str, address: int) -> bool:
        """
        Method that adds the bool constant to the corresponding address
        :param value: bool constant to add
        :type value: str
        :param address: The location to be added
        :type address: int
        :return: If it could added or not
        :rtype: bool
        """
        if value not in self.bools:
            self.bools[value] = address
            return True
        else:
            return False

    def getBool(self, value: str) -> int:
        """
        Get the address of bool
        :param value: the boolean value to add
        :type value: str
        :return: the address where is at
        :rtype: int
        """
        return self.bools[value]

    def get_ctes_table(self) -> dict:
        """
        Method that gets the constant table
        :return: the constant table
        :rtype: dict
        """
        obj = {
            "int" : self.ints,
            "float" : self.floats,
            "string" : self.strings,
            "bool" : self.bools
        }
        return obj

    def print_ctes(self):
        """
        Prints the table constants
        """
        print("Aqui empiezan los INT")
        self.print_tipo(self.ints)
        print("Aqui empiezan los FLOAT")
        self.print_tipo(self.floats)
        print("Aqui empiezan los STRING")
        self.print_tipo(self.strings)
        print("Aqui empiezan los BOOL")
        self.print_tipo(self.bools)