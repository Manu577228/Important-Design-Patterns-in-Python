# The Observer pattern defines a one-to-many dependency. 
# When one object (subject) changes, all its dependents (observers) are notified automatically.

# It’s often used in event systems, GUI libraries, and pub-sub mechanisms.

class Subject:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notify(self, msg):
        for obs in self.observers:
            obs.update(msg)

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print(f"{self.name} received: {msg}")

s = Subject()
o1 = Observer("A")
o2 = Observer("B")
s.register(o1)
s.register(o2)
s.notify("Hello Observers!")
        

