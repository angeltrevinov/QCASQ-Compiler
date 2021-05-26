from VirtualMachine.ExecutionMemory import ExecutionMemory
from GenerateCode.Function_Dir import Function_Dir
from GenerateCode.OpHerarchies import OprTranslator

class VM:

    ex = ExecutionMemory()
    operadores = OprTranslator().OprTrans
    quadruples = []

    def __init__(self, obj: dict):
        #print(obj)
        self.ex.reserve_global_memory(obj["ClassDir"]["varsNum"])
        self.ex.reserve_cte_memory(obj["Constants"])
        self.ex.reserve_local_memory(obj["ClassDir"]["Example"]["function_dir"].get_function("main")["varsNum"])
        #print("Antes de ejecutar quads")
        #self.ex.print_memory()
        self.quadruples = obj["Quadruples"]
        self.execute_quadruples()
        #print("Despues de ejecutar quads")
        #self.ex.print_memory()
        # TODO: add for to execute quads

    def execute_quadruples(self):
        #TODO: change to IP
        for quad in self.quadruples:
            self.resolve_quad(quad)


    def resolve_quad(self, quad: dict):
        if self.operadores["*"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 * op2
            self.ex.save_value(storage[0], storage[1], res)
        elif self.operadores["/"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 / op2
            self.ex.save_value(storage[0], storage[1], res)
        elif self.operadores["+"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 + op2
            self.ex.save_value(storage[0], storage[1], res)
        elif self.operadores["-"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 - op2
            self.ex.save_value(storage[0], storage[1], res)
        elif self.operadores["<"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 < op2
            self.ex.save_value(storage[0], storage[1], res)
        elif self.operadores["<="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 <= op2
            self.ex.save_value(storage[0], storage[1], res)
        elif self.operadores[">"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 > op2
            self.ex.save_value(storage[0], storage[1], res)
        elif self.operadores[">="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 >= op2
            self.ex.save_value(storage[0], storage[1], res)
        elif self.operadores["=="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 == op2
            self.ex.save_value(storage[0], storage[1], res)
        elif self.operadores["!="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 != op2
            self.ex.save_value(storage[0], storage[1], res)
        elif self.operadores["&&"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 and op2
            self.ex.save_value(storage[0], storage[1], res)
        elif self.operadores["||"] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            op2 = quad["operand2"]
            op2 = self.ex.get_value(op2[0], op2[1])
            storage = quad["storage"]
            res = op1 or op2
            self.ex.save_value(storage[0], storage[1], res)
        elif self.operadores["output"] == quad["operator"]:
            storage = quad["storage"]
            print(self.ex.get_value(storage[0], storage[1]))
        elif self.operadores["="] == quad["operator"]:
            op1 = quad["operand1"]
            op1 = self.ex.get_value(op1[0], op1[1])
            storage = quad["storage"]
            self.ex.save_value(storage[0], storage[1], op1)





