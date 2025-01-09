# hw10 store discount
quantity = int(input("Enter your quantity purchased: "))
cost = quantity * 100

if cost >= 1000:
    discount = cost * 10/100
    final_cost = cost - discount    
    print("Total Cost after discount: Rs.", final_cost, sep="")
    print("Discount: Rs.", discount, sep="")
elif cost > 0 and cost < 1000:
    print("Total Cost: Rs.", cost, sep="")
else:
    print("Invalid Quantity")        