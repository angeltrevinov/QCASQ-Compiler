from VirtualMachine.ExecutionMemory import ExecutionMemory
from GenerateCode.Function_Dir import Function_Dir
from GenerateCode.OpHerarchies import OprTranslator

class VM:

    ex = ExecutionMemory()
    operadores = OprTranslator().OprTrans
    quadruples = []

    def __init__(self, obj: dict):
        print(obj)
        self.ex.reserve_global_memory(obj["ClassDir"]["varsNum"])
        self.ex.reserve_cte_memory(obj["Constants"])
        self.ex.reserve_local_memory(obj["ClassDir"]["Example"]["function_dir"].get_function("main")["varsNum"])
        self.ex.print_memory()
        self.quadruples = obj["Quadruples"]
        # TODO: add for to execute quads

    '''def execute_quadruples(self):
        #TODO: change to IP
        for quad in self.quadruples:


    def resolve_quad(self, quad: dict):
        if self.operadores["/"] == quad["operator"]:
            op1 = quad["operand1"][0]'''





