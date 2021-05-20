## Esta clase sera la 'main' controlara toda la VM
from VirtualMachine.Memory import Memory

class VM:
    memory: Memory
    def __init__(self, directory, quadruples):
        self.memory = Memory()
        self.memory.transformDir(directory)
        self.memory.print_memory()

