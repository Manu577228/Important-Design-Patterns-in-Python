# The Builder pattern separates the construction of a complex object from its representation.
# It allows step-by-step object creation.

# Useful when an object has many optional parameters or needs to be built step by step.
# Often used for configuration-heavy objects.

class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None

    def __str__(self):
        return f"Engine: {self.engine}, Wheels: {self.wheels}"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def add_engine(self, engine):
        self.car.engine = engine
        return self

    def add_wheels(self, wheels):
        self.car.wheels = wheels
        return self

    def build(self):
        return self.car


builder = CarBuilder()
car = builder.add_engine("V8").add_wheels(4).build()
print(car)
