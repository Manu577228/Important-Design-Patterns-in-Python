# The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. 
# It allows the algorithm to vary independently from clients.

# It lets you define multiple behaviors and switch them at runtime without modifying the classes using them.

class Add: 
    def operation(self, a, b):
        return a + b
    
class Subtract:
    def operation(self, a, b):
        return a - b
    
class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy.operation(a, b)
    
c1 = Calculator(Add())
print(c1.calculate(10, 5))

c2 = Calculator(Subtract())
print(c2.calculate(10, 5))

