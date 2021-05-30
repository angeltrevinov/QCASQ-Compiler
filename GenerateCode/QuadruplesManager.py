from GenerateCode.OpHerarchies import Operators
from GenerateCode.OpHerarchies import Hierarchies
from GenerateCode.OpHerarchies import OprTranslator
from GenerateCode.SemanticCube import SemanticCube
from GenerateCode.Types import Types
from VirtualMachine.Limits import Limits
import sys

class QuadrupleManager:
    """The controller for handling our Quadruples."""

    # So we can search the hierarchies of incoming operators
    semantic_cube = SemanticCube()
    oprTrans = OprTranslator()
    limits = Limits()
    __operators = Operators().OpHierarchy
    __stack_quadruples__: list   # to control the order of the quadruples quadruples (This needs to be virtual memory)
    __polish_vector__: list    # the help of the polish vector to store our variables
    __stack_operators__: list    # to help for the hierarchy of our operations
    __stack_jumps__: list   # help to control the jumps of non-lineal states

    def __init__(self):
        # create empty arrays to fill while reading the code
        self.__stack_quadruples__ = []
        self.__polish_vector__ = []
        self.__stack_operators__ = []
        self.__stack_jumps__ = []
        self.__add_to_quadruplues__("goto", (), (), ())
        self.__stack_jumps__.append(len(self.__stack_quadruples__) - 1)

    def add_operand(self, variable:int, type: str):
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
        if operator == ")":
            self.__empty_false_stack()
        elif self.__operators[operator] == Hierarchies.GOTOF:
            self.empty_polish_vector()
            op = self.__pop_operand_stack()
            if op[1] != Types.BOOL.value:
                sys.exit(f"The result of an if must be boolean")
            self.__add_to_quadruplues__(operator, op, (), ())
            self.__stack_jumps__.append(len(self.__stack_quadruples__) - 1)
        elif self.__operators[operator] == Hierarchies.GOTO:
            self.__add_to_quadruplues__(operator, (), (), ())
            self.__stack_jumps__.append(len(self.__stack_quadruples__) - 1)
        elif self.__operators[operator] == Hierarchies.GOTOW:
            falso = self.__stack_jumps__.pop()
            ret = self.__stack_jumps__.pop()
            self.__add_to_quadruplues__("goto", (), (), ())
            self.__stack_quadruples__[len(self.__stack_quadruples__) - 1]["storage"] = ret
            self.__stack_quadruples__[falso]["storage"] = (len(self.__stack_quadruples__))
        elif self.__operators[operator] == Hierarchies.ENDFUNC:
            self.__add_to_quadruplues__("endfunc", (), (), ())
        elif self.__operators[operator] == Hierarchies.ERA:
            size = self.__pop_operand_stack()
            self.__add_to_quadruplues__(operator, (), (), size)
        elif self.__operators[operator] == Hierarchies.PARAMS:
            param_dir = self.__pop_operand_stack()
            value = self.__pop_operand_stack()
            if value[1] != param_dir[1]:
                sys.exit(f"Expecting param of type {param_dir[1]} but got {value[1]}")
            self.__add_to_quadruplues__(operator, value, (), param_dir)
        elif self.__operators[operator] == Hierarchies.GOSUB:
            quad_name = self.__pop_operand_stack()
            self.__add_to_quadruplues__(operator, (quad_name[1], ""), (), (quad_name[0], ""))
        elif self.__operators[operator] == Hierarchies.RETURN:
            storage = self.__pop_operand_stack()
            op = self.__pop_operand_stack()
            type = self.semantic_cube.get_result(storage[1], op[1], "=")
            if type == Types.INVALID.value:
                sys.exit(f"You cannot return {op[1]}, expected {storage[1]}")
            self.__add_to_quadruplues__(operator, op, (), storage)
        elif self.__operators[operator] == Hierarchies.ASSIGNRET:
            op = self.__pop_operand_stack()
            self.__add_to_quadruplues__(operator, op, (), (None, op[1]))
        # Check for * or /
        elif self.__operators[operator] == Hierarchies.MULTDIV and len(self.__stack_operators__) > 0:
            # Check if top of the stack has the same hierarchy
            while len(self.__stack_operators__) > 0 and self.__operators[self.__stack_operators__[-1]] == Hierarchies.MULTDIV:
                opr = self.__pop_operator_stack()
                op2 = self.__pop_operand_stack()
                op1 = self.__pop_operand_stack()
                type = self.semantic_cube.get_result(op1[1], op2[1], opr)
                if type == Types.INVALID.value:
                    sys.exit(f"You cannot use the operation {opr} with { op1[1]} and {op2[1]}")
                self.__add_to_quadruplues__(opr, op1, op2, (None, type))
        # Check for + or -
        elif self.__operators[operator] == Hierarchies.SUMSUB and len(self.__stack_operators__) > 0:
            # Check if top of the stack has the same hierarchy or higher
            while (
                    len(self.__stack_operators__) > 0 and
                    (self.__operators[self.__stack_operators__[-1]] == Hierarchies.SUMSUB or
                     self.__operators[self.__stack_operators__[-1]] < Hierarchies.SUMSUB)
            ):
                opr = self.__pop_operator_stack()
                op2 = self.__pop_operand_stack()
                op1 = self.__pop_operand_stack()
                type = self.semantic_cube.get_result(op1[1], op2[1], opr)
                if type == Types.INVALID.value:
                    sys.exit(f"You cannot use the operation {opr} with { op1[1]} and {op2[1]}")

                self.__add_to_quadruplues__(opr, op1, op2, (None, type))
        # check for comparisons
        elif self.__operators[operator] == Hierarchies.COMPARISON and len(self.__stack_operators__) > 0:
            # Check if top of the stack has the same hierarchy or higher
            while (
                    len(self.__stack_operators__) > 0 and
                    (self.__operators[self.__stack_operators__[-1]] == Hierarchies.COMPARISON or
                     self.__operators[self.__stack_operators__[-1]] < Hierarchies.COMPARISON)
            ):
                opr = self.__pop_operator_stack()
                op2 = self.__pop_operand_stack()
                op1 = self.__pop_operand_stack()
                type = self.semantic_cube.get_result(op1[1], op2[1], opr)
                if type == Types.INVALID.value:
                    sys.exit(f"You cannot use the operation {opr} with { op1[1]} and {op2[1]}")
                self.__add_to_quadruplues__(opr, op1, op2, (None, type))
        # check for logic
        elif self.__operators[operator] == Hierarchies.LOGIC and len(self.__stack_operators__) > 0:
            # Check if top of the stack has the same hierarchy or higher
            while (
                    len(self.__stack_operators__) > 0 and
                    (self.__operators[self.__stack_operators__[-1]] == Hierarchies.LOGIC or
                     self.__operators[self.__stack_operators__[-1]] < Hierarchies.LOGIC)
            ):
                opr = self.__pop_operator_stack()
                op2 = self.__pop_operand_stack()
                op1 = self.__pop_operand_stack()
                type = self.semantic_cube.get_result(op1[1], op2[1], opr)
                if type == Types.INVALID.value:
                    sys.exit(f"You cannot use the operation {opr} with {op1[1]} and {op2[1]}")
                self.__add_to_quadruplues__(opr, op1, op2, (None, type))
        # check for OUTPUT
        elif (
                self.__operators[operator] == Hierarchies.OUTPUT
                and len(self.__stack_operators__) > 0
        ):
            self.empty_polish_vector()

        # insert the incoming operator
        if (
                operator != ")" and
                self.__operators[operator] != Hierarchies.GOTOF and
                self.__operators[operator] != Hierarchies.GOTO and
                self.__operators[operator] != Hierarchies.GOTOW and
                self.__operators[operator] != Hierarchies.ENDFUNC and
                self.__operators[operator] != Hierarchies.ERA and
                self.__operators[operator] != Hierarchies.PARAMS and
                self.__operators[operator] != Hierarchies.GOSUB and
                self.__operators[operator] != Hierarchies.RETURN and
                self.__operators[operator] != Hierarchies.ASSIGNRET
        ):
            self.__stack_operators__.append(operator)

    def empty_polish_vector(self):
        """
        Empty the polish vector when we are at the end of the expresion
        """
        # until  the stack operator is empty
        print(self.__polish_vector__)
        print(self.__stack_operators__)
        while len(self.__stack_operators__) > 0:
            if self.__stack_operators__[-1] == "(":
                break
            elif self.__operators[self.__stack_operators__[-1]] == Hierarchies.OUTPUT:
                opr = self.__pop_operator_stack()
                op = self.__pop_operand_stack()
                if (
                        op[1] != Types.BOOL.value and
                        op[1] != Types.INT.value and
                        op[1] != Types.FLOAT.value and
                        op[1] != Types.STRING.value
                ):
                    sys.exit(f"You cannot print a class object")
                self.__add_to_quadruplues__(
                    opr,
                    (),
                    (),
                    op
                )
            elif self.__operators[self.__stack_operators__[-1]] == Hierarchies.ASSIGN:
                opr = self.__pop_operator_stack()
                op1 = self.__pop_operand_stack()  # the data to save
                op2 = self.__pop_operand_stack()  # where to save data
                type = self.semantic_cube.get_result(op1[1], op2[1], opr)
                if type == Types.INVALID.value:
                    sys.exit(f"You cannot assign {op1[1]} to {op2[1]}")
                self.__add_to_quadruplues__(opr, op1, (), op2)
            elif self.__operators[self.__stack_operators__[-1]] == Hierarchies.INPUT:
                opr = self.__pop_operator_stack()
                op  = self.__pop_operand_stack()
                self.__add_to_quadruplues__(opr, (), (), op)
            else:
                opr = self.__pop_operator_stack()
                op2 = self.__pop_operand_stack()
                op1 = self.__pop_operand_stack()
                type = self.semantic_cube.get_result(op1[1], op2[1], opr)
                if type == Types.INVALID.value:
                    sys.exit(f"You cannot use the operation {opr} with {op1[1]} and {op2[1]}")
                self.__add_to_quadruplues__(opr, op1, op2, (None, type))

    def print_quadruples(self):
        for index, quadruple in enumerate(self.__stack_quadruples__):
            print(index, ".-", quadruple["operator"], quadruple["operand1"], quadruple["operand2"], quadruple["storage"])


    def get_quadruples(self):
        return self.__stack_quadruples__

    def completeGoto(self, tipo: str = ""):
        if self.__operators[tipo] == Hierarchies.GOTOF:
            destino = self.__pop_jumps_stack()
            self.__stack_quadruples__[destino]["storage"] = (len(self.__stack_quadruples__))
        else:
            destino = self.__pop_jumps_stack()
            self.__stack_quadruples__[destino]["storage"] = (len(self.__stack_quadruples__) + 1)

    def add_jump_stack(self):
        self.__stack_jumps__.append((len(self.__stack_quadruples__)))


    def __empty_false_stack(self):
        while self.__stack_operators__[-1] != "(":
            opr = self.__pop_operator_stack()
            op2 = self.__pop_operand_stack()
            op1 = self.__pop_operand_stack()
            type = self.semantic_cube.get_result(op1[1], op2[1], opr)
            if type == Types.INVALID.value:
                sys.exit(f"You cannot use the operation {opr} with {op1[1]} and {op2[1]}")
            self.__add_to_quadruplues__(opr, op1, op2, (None, type))
        _ = self.__pop_operator_stack()

    def __pop_operand_stack(self) -> tuple:
        """
        Pops the operand stack and returns the operand
        :return: The operand that has been pop
        :rtype: tuple
        """
        operand = self.__polish_vector__[-1]
        self.__polish_vector__.pop()
        return operand

    def __pop_operator_stack(self) -> str:
        """
        pops the operator in top of the stack
        :return: the operator that has been pop
        :rtype: tuple
        """
        holder = self.__stack_operators__[-1]
        self.__stack_operators__.pop()
        return holder

    def __add_to_quadruplues__(self, operator:str, operand1: tuple, operand2: tuple, storage: tuple):
        """
        Creates the quadruple and inserts it to the stack
        :param operator: the operator for the quadruple
        :type operator: str
        :param operand1: the first operand
        :type operand1: tuple
        :param operand2: the second operand
        :type operand2: tuple
        """
        #print("Here ",storage)
        #print(self.__stack_quadruples__)
        if len(storage) > 0 and storage[0] == None:
            address = self.limits.getAddress(str(storage[1]) + "L") + self.limits.getCont(str(storage[1]) + "L")
            self.limits.check_limits(address, str(storage[1]) + "L")
            self.limits.upCont(str(storage[1]) + "L")
            storage = (address, storage[1])
        elif operator == "era" or operator == "params" or operator == "gosub":
            storage = storage[0]

        self.__stack_quadruples__.append({
            "operator": self.oprTrans.translate(operator),
            "operand1": operand1,
            "operand2": operand2,
            "storage": storage
        })
        if self.__operators[operator] <= Hierarchies.LOGIC or self.__operators[operator] == Hierarchies.ASSIGNRET:
            self.add_operand(storage[0], storage[1])

    def __pop_jumps_stack(self) -> int:
        jump = self.__stack_jumps__[-1]
        self.__stack_jumps__.pop()
        return jump


