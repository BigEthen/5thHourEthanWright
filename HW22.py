#Name:
#Class: 5th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class StoreItem:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
class Store:
    def __init__(self, name, price, stock):
        self.weight = None
        self.name = name
        self.price = price
        self.stock = stock
tshirt = Store("Basic T-Shirt", 15.99, 20)
jeans = Store("Denim Jeans", 49.99, 10)
hat = Store("Baseball Cap", 12.99, 15)
#3. Print the stock of all three objects and the cost of the second store item.
print(tshirt.name, " - Price:", tshirt.price, " - Stock:", tshirt.stock)
print(jeans.name, " - Price:", jeans.price, " - Stock:", jeans.stock)
print(hat.name, " - Price:", hat.price, " - Stock:", hat.stock)
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
def double_cost(self):
    self.cost *= 2
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
hat.stock = int(hat.stock / 4)
print(f"Hat 3 new stock: {hat.stock}")
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del  tshirt.name

try:
    print(f"Weight of tshirt: {tshirt.weight}")
except NameError as e:
    print(f"Error: {e}. tshirt has been deleted.")