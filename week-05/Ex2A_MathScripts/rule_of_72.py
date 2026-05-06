# Rule of 72: Years = 72 / interest rate

savings = 1000
interest_rate = 0.06   # 6%

years = 72 / (interest_rate * 100)
future_value = savings * 2

print("Your current savings is " + str(savings) + ".")
print("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be")
print("worth " + format(future_value, ".2f") + " in " + format(years, ".1f") + " years")