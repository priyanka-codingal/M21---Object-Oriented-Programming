from abc import ABC,abstractmethod

class absclass(ABC):
    def print(self,x):
        print("The value is :" , x)
    
    @abstractmethod
    def task(self):
        print("I am an abstract method")

class test(absclass):
    def task(self):
        print("I am inside test class") 

obj1 = test()
obj1.task()
obj1.print(10)