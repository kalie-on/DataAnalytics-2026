

a = 8
b = 12
c = 10

if a <= b and a <= c:
    smallest = a

elif b <= a and b <= c:
    smallest = b

else:
    smallest = c

if a >= b and a >= c:
    largest = a

elif b >= a and b >= c:
    largest = b

else:
    largest = c

print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")