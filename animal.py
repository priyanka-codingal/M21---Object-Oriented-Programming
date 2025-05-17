from abc import ABC,abstractmethod

class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("I can walk")
    
class dog(animal):
    def move(self):
        print("I can bark")

class snake(animal):
    def move(self):
        print("I can crawl")

obj1 = human()
obj1.move()
obj2 = dog()
obj2.move()
obj3 = snake()
obj3.move()