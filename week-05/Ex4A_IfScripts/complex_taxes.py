

pay_rate = float(input("Enter hourly pay rate: "))
hours_worked = float(input("Enter hours worked: "))
filing_status = input("Enter filing status (single or joint): ")


if hours_worked > 40:
    overtime_hours = hours_worked - 40
    weekly_gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    weekly_gross_pay = hours_worked * pay_rate


annual_gross_income = weekly_gross_pay * 52


if filing_status == "single":

    if annual_gross_income < 12000:
        tax_rate = 0.05

    elif annual_gross_income < 25000:
        tax_rate = 0.10

    elif annual_gross_income < 75000:
        tax_rate = 0.15

    else:
        tax_rate = 0.20


elif filing_status == "joint":

    if annual_gross_income < 12000:
        tax_rate = 0.00

    elif annual_gross_income < 25000:
        tax_rate = 0.06

    elif annual_gross_income < 75000:
        tax_rate = 0.11

    else:
        tax_rate = 0.20


else:
    print("Invalid filing status")
    tax_rate = 0

weekly_tax = weekly_gross_pay * tax_rate

net_pay = weekly_gross_pay - weekly_tax

print(f"\nYou worked {hours_worked} hours this period.")

print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${weekly_gross_pay:.2f}")

print(f"Your estimated annual income is ${annual_gross_income:.2f}")

print(f"Your filing status is {filing_status}")

print(f"Your tax withholding for the week is ${weekly_tax:.2f}")

print(f"Your net pay is ${net_pay:.2f}")