# The Proxy pattern provides a placeholder or surrogate for another object to control access to it.

# Useful for lazy loading, access control, logging, etc., without changing the actual object.

class RealImage:
    def display(self):
        print("Displaying Image")

class ProxyImage:
    def __init__(self):
        self.real_image = None

    def display(self):
        if self.real_image is None:
            print("Loading Image first time")
            self.real_image = RealImage()
        self.real_image.display();

img = ProxyImage();
img.display()
img.display()



