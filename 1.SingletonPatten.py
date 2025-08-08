# The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. 
# This is useful when exactly one object is needed to coordinate actions across the system.

# In Python, you can implement Singleton by overriding the __new__() method or by using decorators/metaclasses. 
# We ensure that the class is instantiated only once — further calls return the same object.

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            print("Using exisiting instance")
        return cls._instance
    
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)

