from GenerateCode.OpHerarchies import Operators
from GenerateCode.OpHerarchies import Hierarchies
from GenerateCode.OpHerarchies import OprTranslator
from GenerateCode.SemanticCube import SemanticCube
from GenerateCode.Types import Types
from VirtualMachine.Limits import Limits
import sys

class QuadrupleManager:
    """
    The controller for handling the construction of our
    Quadruples.

    :Date: 06-02-2021
    :Version: 1
    :Authors:
        - Angel Treviño A01336559
        - Julia Jimenez A00821428
    """

    __stack_quadruples__: list   # to control the order of the quadruples quadruples (This needs to be virtual memory)
    __polish_vector__: list    # the help of the polish vector to store our variables
    __stack_operators__: list    # to help for the hierarchy of our operations
    __stack_jumps__: list   # help to control the jumps of non-lineal states

    semantic_cube = SemanticCube()  # So we can search the hierarchies of incoming operators
    oprTrans = OprTranslator()  # to translate from string to int our operators
    limits = Limits()  # Top check the limits for our addresses
    __operators = Operators().OpHierarchy  # To check the hierarchy of our operators

    def __init__(self):
        # create empty arrays to fill while reading the code
        self.__stack_quadruples__ = []
        self.__polish_vector__ = []
        self.__stack_operators__ = []
        self.__stack_jumps__ = []
        # Generates goto so we can start in main
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
        # to detect if we are in a false stock
        if operator == ")":
            self.__empty_false_stack()
        # To generate quadruple for goto false
        elif self.__operators[operator] == Hierarchies.GOTOF:
            self.empty_polish_vector()
            op = self.__pop_operand_stack()
            if op[1] != Types.BOOL.value:
                sys.exit(f"The result of an if must be boolean")
            self.__add_to_quadruplues__(operator, op, (), ())
            self.__stack_jumps__.append(len(self.__stack_quadruples__) - 1)
        # To generate quadruple for goto
        elif self.__operators[operator] == Hierarchies.GOTO:
            self.__add_to_quadruplues__(operator, (), (), ())
            self.__stack_jumps__.append(len(self.__stack_quadruples__) - 1)
        # To generate quadruple goto while
        elif self.__operators[operator] == Hierarchies.GOTOW:
            falso = self.__stack_jumps__.pop()
            ret = self.__stack_jumps__.pop()
            self.__add_to_quadruplues__("goto", (), (), ())
            self.__stack_quadruples__[len(self.__stack_quadruples__) - 1]["storage"] = ret
            self.__stack_quadruples__[falso]["storage"] = (len(self.__stack_quadruples__))
        # TO generate quadruple for endfunctions
        elif self.__operators[operator] == Hierarchies.ENDFUNC:
            self.__add_to_quadruplues__("endfunc", (), (), ())
        # To generate quadruple for era
        elif self.__operators[operator] == Hierarchies.ERA:
            size = self.__pop_operand_stack()
            self.__add_to_quadruplues__(operator, (), (), size)
        # To generate quadruple for params
        elif self.__operators[operator] == Hierarchies.PARAMS:
            param_dir = self.__pop_operand_stack()
            value = self.__pop_operand_stack()
            # check if the value and the type of params is the same
            if value[1] != param_dir[1]:
                sys.exit(f"Expecting param of type {param_dir[1]} but got {value[1]}")
            self.__add_to_quadruplues__(operator, value, (), param_dir)
        # to generate quadruple for gosubs
        elif self.__operators[operator] == Hierarchies.GOSUB:
            quad_name = self.__pop_operand_stack()
            self.__add_to_quadruplues__(operator, (quad_name[1], ""), (), (quad_name[0], ""))
        # to generate quadruple for return
        elif self.__operators[operator] == Hierarchies.RETURN:
            storage = self.__pop_operand_stack()
            op = self.__pop_operand_stack()
            type = self.semantic_cube.get_result(storage[1], op[1], "=")
            # check if return type is the same as function type
            if type == Types.INVALID.value:
                sys.exit(f"You cannot return {op[1]}, expected {storage[1]}")
            self.__add_to_quadruplues__(operator, op, (), storage)
        # to generate quadruple for assignret
        elif self.__operators[operator] == Hierarchies.ASSIGNRET:
            # the value of global variable for function assign it to the temporal in previous local
            op = self.__pop_operand_stack()
            self.__add_to_quadruplues__(operator, op, (), (None, op[1]))
        # Quad for VER - Array
        elif self.__operators[operator] == Hierarchies.VER:
            limit = self.__pop_operand_stack()
            op = self.__polish_vector__[-1]
            if op[1] != "int":
                sys.exit(f"You can only use integers in an array")
            self.__add_to_quadruplues__(operator, op, (0, "int"), limit)
        # Quad to generate the addbase
        elif self.__operators[operator] == Hierarchies.ADDBASE:
            dir_base = self.__pop_operand_stack()
            op = self.__pop_operand_stack()
            self.__add_to_quadruplues__(operator, op, dir_base, (None, dir_base[1]))
        # Quad that generates the S1 * D2
        elif self.__operators[operator] == Hierarchies.S1D2:
            d2 = self.__pop_operand_stack()
            s1 = self.__pop_operand_stack()
            self.__add_to_quadruplues__(operator, s1, d2, (None, "int"))
        # Quad that generates (S1*D2) + S2
        elif self.__operators[operator] == Hierarchies.S2:
            s1d2 = self.__pop_operand_stack()
            s2 = self.__pop_operand_stack()
            self.__add_to_quadruplues__(operator, s1d2, s2, (None, "int"))
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

        # Dont add this operands to the stack operators array
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
                self.__operators[operator] != Hierarchies.ASSIGNRET and
                self.__operators[operator] != Hierarchies.VER and
                self.__operators[operator] != Hierarchies.ADDBASE and
                self.__operators[operator] != Hierarchies.S1D2 and
                self.__operators[operator] != Hierarchies.S2
        ):
            self.__stack_operators__.append(operator)

    def empty_polish_vector(self):
        """
        Empty the polish vector when we are at the end of the expresion
        """
        # until  the stack operator is empty
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
        """
        Print all quadruples
        """
        for index, quadruple in enumerate(self.__stack_quadruples__):
            print(index, ".-", quadruple["operator"], quadruple["operand1"], quadruple["operand2"], quadruple["storage"])


    def get_quadruples(self):
        """
        Get the quadruples array
        """
        return self.__stack_quadruples__

    def completeGoto(self, tipo: str = ""):
        """
        Function that completes the goto or gotof with the
        quadruple to jump
        :param tipo: the type of goto (goto or gotof)
        :type tipo: str
        """
        if self.__operators[tipo] == Hierarchies.GOTOF:
            destino = self.__pop_jumps_stack()
            self.__stack_quadruples__[destino]["storage"] = (len(self.__stack_quadruples__))
        else:
            destino = self.__pop_jumps_stack()
            self.__stack_quadruples__[destino]["storage"] = (len(self.__stack_quadruples__) + 1)

    def add_jump_stack(self):
        """
        Add the quadruple to the jumpstack so we can resolve it later.
        """
        self.__stack_jumps__.append((len(self.__stack_quadruples__)))

    def __pop_jumps_stack(self) -> int:
        """
        Retrieves the top from the jump stack
        :return: the quadruple index
        :rtype: int
        """
        jump = self.__stack_jumps__[-1]
        self.__stack_jumps__.pop()
        return jump

    def __empty_false_stack(self):
        """
        Method that empties the stack if parenthesis found
        """
        while self.__stack_operators__[-1] != "(":
            opr = self.__pop_operator_stack()
            op2 = self.__pop_operand_stack()
            op1 = self.__pop_operand_stack()
            type = self.semantic_cube.get_result(op1[1], op2[1], opr)
            if type == Types.INVALID.value:
                sys.exit(f"You cannot use the operation {opr} with {op1[1]} and {op2[1]}")
            self.__add_to_quadruplues__(opr, op1, op2, (None, type))
        # removes the "("
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
        # If we need to generate the temporal
        if len(storage) > 0 and storage[0] == None:
            address = self.limits.getAddress(str(storage[1]) + "L") + self.limits.getCont(str(storage[1]) + "L")
            self.limits.check_limits(address, str(storage[1]) + "L")
            self.limits.upCont(str(storage[1]) + "L")
            storage = (address, storage[1])
        # If we have this operators, the storage object is different
        elif operator == "era" or operator == "params" or operator == "gosub" or operator == "ver":
            storage = storage[0]
        # if its add base, we need to indicate is an address
        if operator == "addbase":
            storage = ("(" + str(storage[0]) + ")", storage[1])

        self.__stack_quadruples__.append({
            "operator": self.oprTrans.translate(operator),
            "operand1": operand1,
            "operand2": operand2,
            "storage": storage
        })
        if (self.__operators[operator] <= Hierarchies.LOGIC or
                self.__operators[operator] == Hierarchies.ASSIGNRET or
                self.__operators[operator] == Hierarchies.ADDBASE or
                self.__operators[operator] == Hierarchies.S1D2 or
                self.__operators[operator] == Hierarchies.S2):
            self.add_operand(storage[0], storage[1])


