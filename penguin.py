class bird :
    def __init__(self):
        print("Bird is ready")
    def who(self):
        print("Bird")
    def swim(self):
        print("Birds cant swim")

class penguin(bird) :
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def who(self):
        print("penguin")
    def run(self):
        print("Penguin can run")

obj1 = penguin()
obj1.who()
obj1.swim()
obj1.run()


