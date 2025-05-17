class vehicle :
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(vehicle):
    pass

obj1 = bus("School Volvo",180,29)
print(obj1.name)
print(obj1.max_speed)
print(obj1.mileage)