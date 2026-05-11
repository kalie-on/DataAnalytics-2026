# unoder

my_set = {3,1,2}
print(my_set)

# no dupli
my_set = {1,2,3,3,3,3}
print(my_set)

# mut

my_set = {1,2,3}
my_set.add(4)
print(my_set)

# mut
my_set = {1,2,3}
my_set.remove(2)
print(my_set)

#mut
my_set = {1,2,3}
my_set.discard(2)
print(my_set)

#iterate
my_set = {1,2,3}
for item in my_set:
    print(item)

#unindexable
#my_set = {1,2,3}
#print(my_set[0])




states = {"Texas", "Florida", "California", "New York", "Ohio"}

print(f"Total number of states: {len(states)}")

print(f"Is Texas in the set? {'Texas' in states}")

print(f"States in alphabetical order: {sorted(states)}")

longest_state = max(states, key=len)

print(f"Length of the longest state name: {len(longest_state)}")

states.add("Georgia")
print(f"Updated set after adding Georgia: {states}")

states.discard("Florida")
print(f"Updated set after removing Florida: {states}")



""" day_number = int(input("Enter a number from 1 to 7: "))

if day_number == 1:
    print("Monday")

elif day_number == 2:
    print("Tuesday")

elif day_number == 3:
    print("Wednesday")

elif day_number == 4:
    print("Thursday")

elif day_number == 5:
    print("Friday")

elif day_number == 6:
    print("Saturday")

elif day_number == 7:
    print("Sunday")

else:
    print("Error: must be between 1 and 7.")"""   




total = 0
count = 0

print("Enter positive numbers one at a time.")
print("Enter a negative number to stop.")

number = float(input("Enter a number: "))

while number >= 0:
    total = total + number
    count = count + 1

    number = float(input("Enter a number: "))

print("\nNumbers entered:", count)
print("Sum =", format(total, ".2f"))