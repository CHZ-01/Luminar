class Mobile:
    def __init__(self, brand, model, battery_capacity, storage_capacity, battery_percentage):
        self.brand = str(brand)
        self.model = str(model)
        self.battery_capacity = int(battery_capacity)
        self.storage_capacity = int(storage_capacity)
        self.battery_percentage = int(battery_percentage)

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Capacity: {self.battery_capacity}mAh")
        print(f"Storage Capacity: {self.storage_capacity}GB")
        print(f"Battery Percentage: {self.battery_percentage}%")
    
    def use_battery(self, usage):
        if usage > 0 and usage <= 100:
            self.battery_percentage -= usage
        print(f"Battery percentage after usage: {self.battery_percentage}%")

    def upgrade_storage(self, additional_storage):
        if additional_storage > 0:
            self.storage_capacity += additional_storage
        print(f"Storage Capacity after upgrade: {self.storage_capacity}GB")

mobile1 = Mobile("Samsung", "S24 Ultra", 5000, 256, 95)
mobile1.display_info()
mobile1.use_battery(50)

print()

mobile2 = Mobile("iphone", "16 pro max", 4500, 128, 90)
mobile2.display_info()
mobile2.upgrade_storage(128)