# The Factory pattern provides an interface for creating objects without specifying their concrete classes. 
# It delegates the instantiation to subclasses or functions.

# It allows you to create objects dynamically based on input. 
# You can encapsulate object creation and avoid tight coupling between code and class names.

class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    else:
        raise ValueError("Unknown Animal")
    
a1 = animal_factory("dog")
a2 = animal_factory("cat")

print(a1.speak());
print(a2.speak());
