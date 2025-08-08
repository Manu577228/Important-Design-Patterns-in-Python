# The Decorator pattern allows behavior to be added to an object dynamically without modifying its structure

# In Python, decorators (@) are commonly used to wrap functions to modify their behavior at runtime.

def decorator_func(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator_func
def greet():
    print("Hello Bharadwaj!")

greet()

