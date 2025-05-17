import random 
class fruits_quiz :
    def __init__(self):
        self.fruits = {'apple':'red','mango':'yellow' , 'orange':'orange' , 'grapes':'green' , 'watermelon':'dark green'}
    def quiz(self):
        while True :
            fruit , colour = random.choice(list(self.fruits.items()))
            print("What is the colour of {}".format(fruit))
            user_input = input()
            if user_input.lower() == colour :
                print("correct answer")
            else :
                print("Incorrect answer")
            option = int(input("enter 0 if u wanna continue or 1 to quit"))
            if option :
                break          

print("Welcome to the fruit quizz")
obj1 = fruits_quiz()
obj1.quiz()