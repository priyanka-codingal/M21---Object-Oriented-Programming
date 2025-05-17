class square:
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print("Area is" , self.length * self.length)

class rectangle(square):
    def __init__(self, length, width):
        self.width = width

        square.__init__(self,length)

obj1 = rectangle(4, 5)
obj1.area()
