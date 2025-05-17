class parrot :
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
ob1 = parrot("john",12)
ob2 = parrot("candy",11)

print("John is a",ob1.species)
print("Candy is a",ob2.species)

print(ob1.name,"is",ob1.age,"years old")
print(ob2.name,"is",ob2.age,"years old")
