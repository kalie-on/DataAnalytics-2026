meal_cost = float(input("Enter the cost of the meal: "))
tip = meal_cost * 0.20
tax = meal_cost * 0.0825
total = meal_cost + tip + tax
print("Meal Cost Summary")
print(f"{'Meal Cost:':<50} ${meal_cost:>6.2f}")
print(f"{'Tip (20%):':<50} ${tip:>6.2f}")
print(f"{'Tax (8.25%):':<50} ${tax:>6.2f}")
print(f"{'Total Cost:':<50} ${total:>6.2f}")





students = {
    "caleb" : "DE",
    "nji" : "NY",
    "lee" : "MD"
} 
print(f"caleb : {students['caleb']}")
print(f"nji : {students["nji"]}")
print(f"lee : {students['lee']}")