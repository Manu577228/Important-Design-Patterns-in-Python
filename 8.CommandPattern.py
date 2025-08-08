# The Command pattern encapsulates a request as an object, 
# allowing you to parameterize clients, queue, or log requests.

# It decouples the sender from the receiver of the command and provides undo/redo capabilities.

class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")

class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

light = Light()
cmd = LightOnCommand(light)
cmd.execute()
