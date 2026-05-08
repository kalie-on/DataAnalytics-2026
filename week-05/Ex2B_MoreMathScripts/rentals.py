
import math

people = int(input("Enter number of people going on the tour: "))

van_capacity = 15
van_cost = 250

vans_needed = math.ceil(people / van_capacity)
total_cost = vans_needed * van_cost
cost_per_person = total_cost / people

print(f"Vans needed: {vans_needed}")
print(f"Total van cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")

# a) How much money did your script say you had to charge per person?

# 19.4

# b) If you multiply that out, how much did you collect?
 
cost = 19.74
person = 38
print(f"total colected ${cost * person:.2f}" )


# c) How much were the vans?
# 750

# d) Why do you have leftover money

# because each person pays a rounded amount, but the real exact cost is $750 / 38 = $19.7368
# When round to $19.74, you collect a little more than $750.