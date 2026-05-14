import statistics  # standard library — no install needed

def analyze_sales(analyst, region, sales):

    mean = statistics.mean(sales)
    median = statistics.median(sales)
    mode = statistics.mode(sales)
    stdev = statistics.stdev(sales)

    total = sum(sales)   # built-in — no import needed
    high = max(sales)    # built-in
    low = min(sales)     # built-in

    return mean, median, mode, stdev, total, high, low


analyst = input("Analyst name: ")
region = input("Region: ")

print("Enter daily sales for 7 days (one per line):")

sales = [float(input(f" Day {i+1}: $")) for i in range(7)]


mean, median, mode, stdev, total, high, low = analyze_sales(
    analyst,
    region,
    sales
)


print(f"""

Analyst : {analyst}
Region  : {region}
Data    : {sales}


Total revenue : ${total:.2f}
Mean (avg)    : ${mean:.2f}
Median        : ${median:.2f}
Mode          : ${mode:.2f}
Std deviation : ${stdev:.2f}
Highest day   : ${high:.2f}
Lowest day    : ${low:.2f}
""")