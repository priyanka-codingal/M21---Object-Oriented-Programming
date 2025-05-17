class vehicle :
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

ob = vehicle(180,20)

print("The max speed of the vehicle is",ob.max_speed)
print("The mileage of the vehicle is",ob.mileage)
