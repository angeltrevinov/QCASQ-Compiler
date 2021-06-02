import sys

from VirtualMachine.ExecutionMemory import ExecutionMemory
from GenerateCode.OpHerarchies import OprTranslator

class VM:
    """
    Virtual Machine class that receives the information from
    the parser, and executes the quadruples created in parser
    to execute the program inside the input file.

    :Date: 06-02-2021
    :Version: 1
    :Authros:
        - Angel Treviño A01336559
        - Julia Jimenez A00821428
    """

    ex = ExecutionMemory()  # object that controls the memory in execution
    operadores = OprTranslator().OprTrans  # object that helps us transform operator num

    quadruples = []    # list that stores the quadruples so we can execute each line
    program_name: str  # To store the program name, so we can search in our class directory
    class_dir : dict  # Our class directory
    IP: int  # The instruction pointer that points to a quadruple in the array.

    def __init__(self, obj: dict):
        """
        Constructor that extras the information that the parse
        has retrieve
        :param obj: The object that the parser send with variables info and quadruples
        :type obj:  dict
        """
        self.ex.reserve_global_memory(obj["ClassDir"]["varsNum"])
        self.ex.reserve_cte_memory(obj["Constants"])
        self.class_dir = obj["ClassDir"]
        self.program_name = list(self.class_dir)[0]
        self.ex.reserve_local_memory(
            self.class_dir[self.program_name]["function_dir"].get_function("main")["varsNum"]
        )
        self.ex.set_new_memory_to_local()
        self.quadruples = obj["Quadruples"]
        self.execute_quadruples()

    def execute_quadruples(self):
        """
        Navigates the quadruples based on the instruction pointer
        until we have reach the end of our quadruples.
        """
        self.IP = 0
        while self.IP < len(self.quadruples):
            self.resolve_quad(self.quadruples[self.IP])

    def resolve_quad(self, quad: dict):
        """
        Method that performs the operation indicated inside the quad
        :param quad: The quad we are currently working on
        :type quad: dict
        """
        # --------------- MULTIPLICATION -------------------
        if self.operadores["*"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 * op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # ----------------- DIVISION -----------------------
        elif self.operadores["/"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 / op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # ------------------- SUM --------------------------
        elif self.operadores["+"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 + op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # ----------------- SUBTRACTION --------------------
        elif self.operadores["-"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 - op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # --------------- LESS THAN ------------------------
        elif self.operadores["<"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 < op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # ------------- LESS or EQUAL THAN -----------------
        elif self.operadores["<="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 <= op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # -------------- GREATER THAN ----------------------
        elif self.operadores[">"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 > op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # ----------- GREATER or EQUAL THAN ----------------
        elif self.operadores[">="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 >= op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # ----------------- EQUAL --------------------------
        elif self.operadores["=="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 == op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # ------------- DIFFERENT THAN ---------------------
        elif self.operadores["!="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 != op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # ------------------- AND --------------------------
        elif self.operadores["&&"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 and op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # ------------------ OR ----------------------------
        elif self.operadores["||"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 or op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # ------------------ OUTPUT ------------------------
        elif self.operadores["output"] == quad["operator"]:
            storage = quad["storage"]
            print(self.ex.get_value(storage[0], storage[1]))
            self.IP = self.IP + 1
        # ----------------- INPUT --------------------------
        elif self.operadores["input"] == quad["operator"]:
            storage = quad["storage"]
            res = input("> ")
            res = self.ex.cast_type(storage[1], res)
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        # ---------------- ASSIGN --------------------------
        elif self.operadores["="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            storage = quad["storage"]
            self.ex.save_value(storage[0], storage[1], op1)
            self.IP = self.IP + 1
        # ----------------- GOTOF --------------------------
        elif self.operadores["gotof"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            if op1 == False:
                self.IP = quad["storage"]
            else:
                self.IP = self.IP + 1
        # ----------------- GOTO ---------------------------
        elif self.operadores["goto"] == quad["operator"]:
            self.IP = quad["storage"]
        # ------------------ ERA ---------------------------
        elif self.operadores["era"] == quad["operator"]:
            self.ex.reserve_local_memory(
                self.class_dir[self.program_name]["function_dir"].get_function(
                    quad["storage"]
                )["varsNum"]
            )
            self.IP = self.IP + 1
        # ---------------- PARAMS --------------------------
        elif self.operadores["params"] == quad["operator"]:
            # obtain the value to pass from memory
            value_to_pass = self.ex.get_value(quad["operand1"][0], quad["operand1"][1])
            # save the value in the memory for that function
            self.ex.pass_params_to_new(quad["storage"], quad["operand1"][1], value_to_pass)
            self.IP = self.IP + 1
        # ------------------ GOSUB -------------------------
        elif self.operadores["gosub"] == quad["operator"]:
            self.ex.save_memory(self.IP)
            self.ex.set_new_memory_to_local()
            self.IP = quad["storage"]
        # ----------------- ENDFUNC ------------------------
        elif self.operadores["endfunc"] == quad["operator"]:
            self.IP = self.ex.restore_previous_memory()
            self.IP = self.IP + 1
        # ------------------ RETURN ------------------------
        elif self.operadores["return"] == quad["operator"]:
            value_to_pass = quad["operand1"]
            value_to_pass = self.ex.get_value(value_to_pass[0], value_to_pass[1])
            storage = quad["storage"]
            self.ex.save_value(storage[0], storage[1], value_to_pass)
            self.IP = self.IP + 1
        # ----------------- ARRSIGNRET ---------------------
        elif self.operadores["assignret"] == quad["operator"]:
            value_to_pass = quad["operand1"]
            value_to_pass = self.ex.get_value(value_to_pass[0], value_to_pass[1])
            storage = quad["storage"]
            self.ex.save_value(storage[0], storage[1], value_to_pass)
            self.IP = self.IP + 1
        # ----------------- VER ----------------------------
        elif self.operadores["ver"] == quad["operator"]:
            operand1 = quad["operand1"]
            low_limit = quad["operand2"][0]
            higher_limit = quad["storage"]
            value_to_check = self.ex.get_value(operand1[0], operand1[1])
            if value_to_check < low_limit or value_to_check >= higher_limit:
                sys.exit(f"Error: Index out of range, value: {value_to_check} for limits {low_limit} and {higher_limit}")
            self.IP = self.IP + 1
        elif self.operadores["addbase"] == quad["operator"]:
            operand1 = quad["operand1"]
            operand1 = self.ex.get_value(operand1[0], operand1[1])
            base = quad["operand2"][0]
            storage = quad["storage"]
            storage = (quad["storage"][0][1:-1], quad["storage"][1])
            dir_final = operand1 + base
            self.ex.save_value(int(storage[0]), storage[1], dir_final)
            self.IP = self.IP + 1
        elif self.operadores["s1d2"] == quad["operator"]:
            operand1 = quad["operand1"]
            operand1 = self.ex.get_value(operand1[0], operand1[1])
            operand2 = quad["operand2"]
            #operand2 = self.ex.get_value(operand2[0], operand2[1])
            storage = quad["storage"]
            res = operand1 * operand2[0]
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores["s2"] == quad["operator"]:
            operand1 = quad["operand1"]
            operand1 = self.ex.get_value(operand1[0], operand1[1])
            operand2 = quad["operand2"]
            operand2 = self.ex.get_value(operand2[0], operand2[1])
            storage = quad["storage"]
            res = operand1 + operand2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1



