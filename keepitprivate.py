class class1 :
    __privatevar = 12

    def __privmeth(self) :
        print("I am a private method")
    
    def hello(self):
        print("The value of privatevar is :", class1.__privatevar)
    
obj1 = class1()
obj1.hello()
obj1.__privmeth()