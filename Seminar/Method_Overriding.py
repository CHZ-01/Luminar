# Defining parent class
class Bird:
    # Defining methods
    def intro(self):
        print("There are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some cannot.")

# Defining child classes of Bird class
class sparrow(Bird):
    # Overriding flight method
    def flight(self):
        print("Sparrows can fly.")

# Creating object for Bird class
obj_bird = Bird()
# Calling methods of Bird class
obj_bird.intro()
# Before Overriding
obj_bird.flight()

print()

# Creating object for sparrow class
obj_spr = sparrow()
# Calling methods of sparrow class
obj_spr.intro()
# After Overriding
obj_spr.flight()