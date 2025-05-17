class person:
    def __init__(self,name, id_number):
        self.name = name
        self.id_number = id_number
    
    def display(self):
        print(self.name)
        print(self.id_number)

class employee(person):
    def __init__(self , name, id_number , salary , post):
        self.salary = salary
        self.post = post

        person.__init__(self,name, id_number)

obj1 = employee("adi" , 12675494 , 10000000 , "ceo")
obj1.display()