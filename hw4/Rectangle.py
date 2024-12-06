# Dallin Moore
# https://chat.openai.com/share/6ea8ab16-d29e-470f-9ae1-f114c5cd0cc1

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
        
rectangle1 = Rectangle(5,3)
print(rectangle1.area())