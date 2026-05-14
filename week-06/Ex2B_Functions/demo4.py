# Ndifon
# 05/09/26

from datetime import date, time, datetime, timedelta, timezone

# date(year, month, day)
today = date(2026, 5, 9)
print("Date:", today)

# time(hour, minute, second, microsecond)
current_time = time(14, 30, 45)
print("Time:", current_time)

# datetime(year, month, day, hour, minute, second)
current_datetime = datetime(2026, 5, 9, 14, 30)
print("Datetime:", current_datetime)

# timedelta(days, hours, minutes, weeks, etc.)
future_date = today + timedelta(days=7)
print("Future Date:", future_date)

# timezone(timedelta(hours=offset))
est = timezone(timedelta(hours=-5))

# datetime.now(timezone)
utc_time = datetime.now(timezone.utc)
print("UTC Time:", utc_time)


import statistics

# Sample dataset
data = [10, 20, 20, 40, 50]

print("=== Python Statistics Module Demo ===\n")

# mean() -> average value
print("mean:", statistics.mean(data))

# median() -> middle value
print("median:", statistics.median(data))

# mode() -> most common value
print("mode:", statistics.mode(data))

# stdev() -> standard deviation (sample)
print("stdev:", statistics.stdev(data))

# variance() -> variance (sample)
print("variance:", statistics.variance(data))


# lambda arguments: expression
# contains any number of arguments but contains only one expression.

# Lambda function to double a number
doubler = lambda n: n * 2

print(doubler(5))


# Lambda function to add a number
add_numbers = lambda a, b: a + b

print(add_numbers(3, 7))


# Lambda function to determine largest number
largest = lambda x, y: x if x > y else y

print(largest(12, 8))