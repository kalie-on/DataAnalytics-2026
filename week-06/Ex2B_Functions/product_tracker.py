

class Products:
    def __init__(self,name,category,price,quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product name: {self.name}")
        print(f"category: {self.category}")
        print(f"price: ${self.price:.2f}")
        print(f"quantity: {self.quantity} units")
        print("____________________")


    def inventory_value(self):

        total = self.price * self.quantity

        print(f"Inventory value for {self.name}: ${total:.2f}")
        print("-----------------------------")


print("=== Enter Product 1 ===")

name1 = input("Product name: ")
category1 = input("Category: ")
price1 = float(input("Price $: "))
quantity1 = int(input("Quantity: "))

print("\n=== Enter Product 2 ===")

name2 = input("Product name: ")
category2 = input("Category: ")
price2 = float(input("Price $: "))
quantity2 = int(input("Quantity: "))

product1 = Products(name1, category1, price1, quantity1)
product2 = Products(name2, category2, price2, quantity2)


