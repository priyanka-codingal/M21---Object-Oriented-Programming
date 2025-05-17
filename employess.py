class employee :
    def __init__(self):
        print("Employee Created")
    def __del__(self):
        print("Destructor Called")

def createobj():
    print("making the object")
    ob=employee()
    print("function ends")
    return ob

print("Calling creatobj function")
ob1 = createobj()
print("Program ends")
