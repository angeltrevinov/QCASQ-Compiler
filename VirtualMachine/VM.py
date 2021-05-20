## Esta clase sera la 'main' controlara toda la VM
from VirtualMachine.Memory import Memory

class VM:
    memory: Memory
    def __init__(self, directory, quadruples):
        self.memory = Memory()
        self.memory.save_global_vars(directory)
        self.memory.print_memory()

