class India:
    def capital(self):
        print("The capital of India is New delhi")
    def language(self):
        print("The native language of India is Hindi")
    def type(self):
        print("India is a developing country")

class USA:
    def capital(self):
        print("The capital of USA is Washington DC")
    def language(self):
        print("The native language of USA is English")
    def type(self):
        print("USA is a developed country")

obj1 = India()
obj2 = USA()

for country in ( obj1 , obj2 ):
    country.capital()
    country.language()
    country.type()

