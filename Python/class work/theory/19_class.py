# self used to create unique locations for every variables

class car:
    company = "BMW" # class variable
    no_of_tyres = 4 # class variable

    def __init__(self,color,speed): # constructor, always get executed without calling
        self.color = color # instance variable
        self.speed = speed # instance variable
    
# objects i.e real instance of a class
obj1 = car("black",150) 
obj2 = car("red",120)

# obj1 properties
print(obj1.color, obj1.speed, obj1.company, obj1.no_of_tyres)

# obj2 properties
print(obj2.color, obj2.speed, obj2.company, obj2.no_of_tyres)