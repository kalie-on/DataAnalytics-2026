

sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25),
]

total_sales = 0

for name, region, sales in sales_data:

    print(name, "(" + region + "): $" + format(sales, ",.2f"))

    if sales > 5000:
        print("^ Top performer!")

    total_sales = total_sales + sales

print("Overall Total Sales: $" + format(total_sales, ",.2f"))