from GenerateCode.CteTable import CteTable
from GenerateCode.Class_Dir import Class_Dir
from GenerateCode.QuadruplesManager import QuadrupleManager

class Memory:

    def __init__(self, ctes: CteTable, dir_func: Class_Dir, quads: QuadrupleManager):
        self.pasarCtes(ctes)

    def pasarCtes(self, ctes: CteTable):
        print(ctes)

    #def pasarDir(self, dir_func: Class_Dir):

    #def pasarQuads(self, quads: QuadrupleManager):

