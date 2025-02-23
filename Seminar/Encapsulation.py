# Creating a Parent class
class Base:
    def __init__(self):
        self.a = "public" # no underscore
        self._b = "protected" # single underscore
        self.__c = "private" # two underscores

    def setting(self, value):
        self.__c = value

    def getting(self):
        return self.__c

# Creating a Child class
class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        # accessing public variable
        print("Calling public member of base class: ",self.a) 
        # accessing protected variable
        print("Calling protected member of base class: ",self._b)
        # accessing private variable, shows error message 
        # print("Calling private member of base class: ",self.__c) 

# Creating an object of the child class
obj = Derived()
obj.setting("python")
print(obj.getting())