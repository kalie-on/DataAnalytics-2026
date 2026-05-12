

# Ndifon Caleb Ndakina
# Sales Summary Calculator
# Concepts: user input, f-string, type cast, user-defined function

def sales_summary(name, region, units, price):
    revenue = units * price
    bonus = revenue * 0.10
    return revenue, bonus

# Collect input
name = input("Associate name: ")
region = input("Store region: ")

units = int(input("Units sold: "))
price = float(input("Price per unit $: "))


# Call the function
revenue, bonus = sales_summary(name, region, units, price)

# Print formatted report
print(f"""

Associate : {name}
Region : {region}
Units sold: {units}
Unit price: ${price:.2f}

Total revenue : ${revenue:.2f}
Performance bonus (10%) : ${bonus:.2f}
""")