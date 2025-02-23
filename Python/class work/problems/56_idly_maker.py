class Idly_Maker:
    def __init__(self, size, num_idlies, cooked, overcooked):
        self.size = size
        self.num_idlies = num_idlies
        self.cooked = cooked
        self.overcooked = overcooked

    def add_toppings(self, toppings):
        self.toppings = toppings.split(",")

    def cook(self, time):
        self.time = time

        if self.size == "Small":
            if self.time >= 8:
                self.overcooked = True
            else:
                self.overcooked = False

            if self.time < 8 and self.time >= 5:
                self.cooked = True
            else:
                self.cooked = False

        elif self.size == "Medium":
            if self.time >= 10:
                self.overcooked = True
            else:
                self.overcooked = False

            if self.time < 10 and self.time >= 7:
                self.cooked = True
            else:
                self.cooked = False

        elif self.size == "Large":
            if self.time >= 13:
                self.overcooked = True
            else:
                self.overcooked = False

            if self.time < 13 and self.time >= 10:
                self.cooked = True
            else:
                self.cooked = False

    def display_idly(self):
        print("IDLI Details")
        print(f"Size: {self.size}")
        print(f"No of Idlies: {self.num_idlies}")
        print(f"Toppings: {self.toppings}")
        print(f"Cooked: {self.cooked}")
        print(f"OverCooked: {self.overcooked}")

idly1 = Idly_Maker("Small", 7, False, False)
idly1.add_toppings("Chutney,Tomato")
idly1.cook(6)
idly1.display_idly()

print()

idly2 = Idly_Maker("Medium", 5, False, False)
idly2.add_toppings("Carrot,Sambar")
idly2.cook(7)
idly2.display_idly()

print()

idly3 = Idly_Maker("Large", 3, False, False)
idly3.add_toppings("Chutney,Sambar")
idly3.cook(13)
idly3.display_idly()