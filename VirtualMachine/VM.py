from VirtualMachine.ExecutionMemory import ExecutionMemory
from GenerateCode.Function_Dir import Function_Dir
from GenerateCode.OpHerarchies import OprTranslator
from GenerateCode.SemanticCube import SemanticCube
from GenerateCode.Types import Types
import sys

class VM:

    ex = ExecutionMemory()
    operadores = OprTranslator().OprTrans
    quadruples = []
    semanticCube = SemanticCube()
    program_name: str
    class_dir : dict
    IP: int

    def __init__(self, obj: dict):
        #print(obj)
        self.ex.reserve_global_memory(obj["ClassDir"]["varsNum"])
        self.ex.reserve_cte_memory(obj["Constants"])
        self.class_dir = obj["ClassDir"]
        self.program_name = list(self.class_dir)[0]
        self.ex.reserve_local_memory(self.class_dir[self.program_name]["function_dir"].get_function("main")["varsNum"])
        self.ex.set_new_memory_to_local()
        #print("Antes de ejecutar quads")
        #self.ex.print_memory()
        self.quadruples = obj["Quadruples"]
        self.execute_quadruples()
        #print("Despues de ejecutar quads")
        #self.ex.print_memory()

    def execute_quadruples(self):
        self.IP = 0
        while self.IP < len(self.quadruples):
            self.resolve_quad(self.quadruples[self.IP])


    def resolve_quad(self, quad: dict):
        if self.operadores["*"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 * op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores["/"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 / op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores["+"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 + op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores["-"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 - op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores["<"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 < op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores["<="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 <= op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores[">"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 > op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores[">="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 >= op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores["=="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 == op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores["!="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 != op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores["&&"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 and op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores["||"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 or op2
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores["output"] == quad["operator"]:
            storage = quad["storage"]
            print(self.ex.get_value(storage[0], storage[1]))
            self.IP = self.IP + 1
        elif self.operadores["input"] == quad["operator"]:
            storage = quad["storage"]
            res = input(">")
            res = self.ex.cast_type(storage[1], res)
            self.ex.save_value(storage[0], storage[1], res)
            self.IP = self.IP + 1
        elif self.operadores["="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            storage = quad["storage"]
            self.ex.save_value(storage[0], storage[1], op1)
            self.IP = self.IP + 1
        elif self.operadores["gotof"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            if op1 == False:
                self.IP = quad["storage"]
            else:
                self.IP = self.IP + 1
        elif self.operadores["goto"] == quad["operator"]:
            self.IP = quad["storage"]
        elif self.operadores["era"] == quad["operator"]:
            self.ex.reserve_local_memory(self.class_dir[self.program_name]["function_dir"].get_function(quad["storage"])["varsNum"])
            self.IP = self.IP + 1
        elif self.operadores["params"] == quad["operator"]:
            value_to_pass = self.ex.get_value(quad["operand1"][0], quad["operand1"][1])
            self.ex.pass_params_to_new(quad["storage"], quad["operand1"][1], value_to_pass)
            self.IP = self.IP + 1
        elif self.operadores["gosub"] == quad["operator"]:
            self.ex.save_memory(self.IP)
            self.ex.set_new_memory_to_local()
            self.IP = quad["storage"]
        elif self.operadores["endfunc"] == quad["operator"]:
            self.IP = self.ex.restore_previous_memory()
            self.IP = self.IP + 1



