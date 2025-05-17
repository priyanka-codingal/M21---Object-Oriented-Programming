class IOstring:
    def __init__(self):
        self.str1 = ""
    def getstring(self):
        self.str1 = input("Enter a word : ")
    def printstring(self):
        print("The uppercased format is : " , self.str1.upper())

ob1 = IOstring()
ob1.getstring()
ob1.printstring()