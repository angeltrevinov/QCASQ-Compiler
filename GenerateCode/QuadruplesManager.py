class QuadrupleManager:
    """The controller for handling our Quadruples."""
    __stack_quadruples__: list   # to control the order of the quadruples quadruples
    __stack_types__: list
    __polish_vector__: list    # the help of the polish vector to store our variables
    __stack_operators__: list    # to help for the hierarchy of our operations

    def __init__(self):
        # create empty arrays to fill while reading the code
        self.__stack_quadruples__ = []
        self.__polish_vector__ = []
        self.__stack_types__ = []
        self.__stack_operators__ = []

    def __add_to_pv(self, operand: str):
        self.__polish_vector__.append(operand)

    def __add_to_types(self, type: str):
        self.__stack_types__.append(type)

    def add_operand(self, variable:str, type: str):
        self.__add_to_pv(variable)
        self.__add_to_types(type)

    def add_to_stack_op(self, operator: str):
        # TODO: ADD verifications
        self.__polish_vector__.append(operator)

    def add_to_quadruplues__(self, operator:str, operand1:str, operand2: str):
        self.__stack_quadruples__.append({
            "operator": operator,
            "operand1": operand1,
            "operand2": operand2,
            "storage": "something"
        })