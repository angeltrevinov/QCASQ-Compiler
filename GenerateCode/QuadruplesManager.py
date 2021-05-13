from GenerateCode.OpHerarchies import Operators

class QuadrupleManager:

    __operators = Operators().Herarchy

    """The controller for handling our Quadruples."""
    __stack_quadruples__: list   # to control the order of the quadruples quadruples
    __polish_vector__: list    # the help of the polish vector to store our variables
    __stack_operators__: list    # to help for the hierarchy of our operations

    def __init__(self):
        # create empty arrays to fill while reading the code
        self.__stack_quadruples__ = []
        self.__polish_vector__ = []
        self.__stack_operators__ = []

    def add_operand(self, variable:str, type: str):
        self.__polish_vector__.append((variable, type))

    def __pop_operand_stack(self):
        operand = self.__polish_vector__[-1]
        self.__polish_vector__.pop()
        return  operand

    def __pop_operator_stack(self):
        holder = self.__stack_operators__[-1]
        self.__stack_operators__.pop()
        return holder


    def add_to_stack_op(self, operator: str):
        # TODO: ADD verifications
        if operator == ",":# change commas to outputs
            operator = "output"
        if self.__operators[operator] == 1:  # * or / appeared
            while self.__operators[self.__stack_operators__[-1]] == 1: # check if top of the stack has the same herarchy
                opr = self.__pop_operator_stack()
                # TODO Check operands types
                op2 = self.__pop_operand_stack()
                op1 = self.__pop_operand_stack()
                self.add_to_quadruplues__(opr, op1, op2)

        self.__stack_operators__.append(operator)

    def add_to_quadruplues__(self, operator:str, operand1:str, operand2: str):
        self.__stack_quadruples__.append({
            "operator": operator,
            "operand1": operand1,
            "operand2": operand2,
            "storage": "t" + str(len(self.__stack_quadruples__)) # TODO: This needs to be a memory
        })
        self.add_operand(self.__stack_quadruples__[-1]["storage"], "int")