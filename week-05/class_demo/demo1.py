# Ndifon Caleb N
# 5/4/2026

name = "Caleb" 
age = 22

print(name)
print(age)

print(f'my name is {name} and i am {age}')

pi = 3.145678

print(f"the value of pi is {pi:.2f}")

sale = 12345.7685
print(f"the value of sale is ${sale:,.2f}")



original_price = float(input("Enter the original price: "))

discount_percent = float(input("Enter the discount percentage: "))

discount_amount = (discount_percent / 100) * original_price

final_price = original_price - discount_amount

print(f"The final price after a {discount_percent:.0f}% discount is: ${final_price:.2f}")
