pay_rate = 20.75
hours_worked = 35

if hours_worked >40:
    overtime = hours_worked - 40
    gross_pay= (hours_worked * pay_rate) + (overtime * pay_rate * 1.5)
else:
    gross_pay = hours_worked * pay_rate

print(f"gross_pay is ${gross_pay:.2f}")