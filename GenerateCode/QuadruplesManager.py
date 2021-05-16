from GenerateCode.OpHerarchies import Operators
from GenerateCode.OpHerarchies import Hierarchies

class QuadrupleManager:
    """The controller for handling our Quadruples."""

    # So we can search the hierarchies of incoming operators
    __operators = Operators().OpHierarchy
    __stack_quadruples__: list   # to control the order of the quadruples quadruples (This needs to be virtual memory)
    __polish_vector__: list    # the help of the polish vector to store our variables
    __stack_operators__: list    # to help for the hierarchy of our operations

    def __init__(self):
        # create empty arrays to fill while reading the code
        self.__stack_quadruples__ = []
        self.__polish_vector__ = []
        self.__stack_operators__ = []

    def add_operand(self, variable:str, type: str):
        """
        Method that adds the operand and its type to the polish vector

        :param variable: the name of the variable
        :type variable: str
        :param type: the type of variable
        :type type: str
        """
        self.__polish_vector__.append((variable, type))

    def add_to_stack_op(self, operator: str):
        """
        Method that adds the operator to the stack operator
        :param operator: the operator that is coming
        :type operator: str
        """
        # change commas to output operators
        if operator == ",":
            operator = "output"
        # Check for * or /
        if self.__operators[operator] == Hierarchies.MULTDIV:
            # Check if top of the stack has the same hierarchy
            while self.__operators[self.__stack_operators__[-1]] == Hierarchies.MULTDIV:
                opr = self.__pop_operator_stack()
                # TODO Check operands types
                op2 = self.__pop_operand_stack()
                op1 = self.__pop_operand_stack()
                self.__add_to_quadruplues__(opr, op1, op2)
        # Check for + or -
        elif self.__operators[operator] == Hierarchies.SUMSUB:
            # Check if top of the stack has the same hierarchy or higher
            while (
                    self.__operators[self.__stack_operators__[-1]] == Hierarchies.SUMSUB or
                    self.__operators[self.__stack_operators__[-1]] < Hierarchies.SUMSUB
            ):
                opr = self.__pop_operator_stack()
                # TODO Check operands types
                op2 = self.__pop_operand_stack()
                op1 = self.__pop_operand_stack()
                self.__add_to_quadruplues__(opr, op1, op2)
        # insert the incoming operator
        self.__stack_operators__.append(operator)

    def empty_polish_vector(self):
        """
        Empty the polish vector when we are at the end of the expresion
        """
        # until  the stack operator is empty
        while len(self.__stack_operators__) > 0:
            opr = self.__pop_operator_stack()
            # TODO Check operands types
            op2 = self.__pop_operand_stack()
            op1 = self.__pop_operand_stack()
            # TODO Becareful with assigns
            self.__add_to_quadruplues__(opr, op1, op2)

    def __pop_operand_stack(self) -> tuple:
        """
        Pops the operand stack and returns the operand
        :return: The operand that has been pop
        :rtype: tuple
        """
        operand = self.__polish_vector__[-1]
        self.__polish_vector__.pop()
        return operand

    def __pop_operator_stack(self) -> tuple:
        """
        pops the operator in top of the stack
        :return: the operator that has been pop
        :rtype: tuple
        """
        holder = self.__stack_operators__[-1]
        self.__stack_operators__.pop()
        return holder

    def __add_to_quadruplues__(self, operator:str, operand1: tuple, operand2: tuple):
        """
        Creates the quadruple and inserts it to the stack
        :param operator: the operator for the quadruple
        :type operator: str
        :param operand1: the first operand
        :type operand1: tuple
        :param operand2: the second operand
        :type operand2: tuple
        """
        self.__stack_quadruples__.append({
            "operator": operator,
            "operand1": operand1,
            "operand2": operand2,
            "storage": "t" + str(len(self.__stack_quadruples__)) # TODO: This needs to be a memory
        })
        self.add_operand(self.__stack_quadruples__[-1]["storage"], "int")
