# # Design a class named ShoppingCart in Python that represents a shopping cart in an e-commerce

class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_name, quantity, price):
        self.items[item_name] = (quantity, price)

    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.pop(item_name)
        else:
            print("Item not found in the cart.")

    def update_quantity(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] = (quantity, self.items[item_name][1])
        else:
            print("Item not found in the cart.")

    def get_total_cost(self):
        cost = 0
        for i in self.items:
            cost += self.items[i][1]
        print("Total cost:", cost)

    def list_items(self):
        print("Items in the cart:")
        for i in self.items:
            print(f"{i}: Quantity - {self.items[i][0]}, Price - {self.items[i][1]}")

purchase1 = ShoppingCart()

purchase1.add_item("Apple", 2, 10)
purchase1.add_item("Banana", 3, 7)
purchase1.add_item("Orange", 1, 8)
purchase1.add_item("Carrot", 1, 5)

purchase1.remove_item("Carrot")
purchase1.update_quantity("Apple", 4)
purchase1.get_total_cost()
purchase1.list_items()