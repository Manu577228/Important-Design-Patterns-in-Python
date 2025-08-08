# The Facade pattern provides a simplified interface to a complex subsystem.

# It hides internal complexities and provides a unified entry point to interact with multiple modules.

class CPU:
    def start(self):
        print("CPU Started")

class Memory:
    def load(self):
        print("Memory Loaded")

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()

    def start_computer(self):
            self.cpu.start()
            self.memory.load()

pc = Computer()
pc.start_computer()