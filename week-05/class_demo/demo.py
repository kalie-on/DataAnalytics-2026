

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (9 / 5) * celsius + 32

print(f"Fahrenheit = {fahrenheit:.2f}")


# count

t = (1,2,2,3,2)
print(t.count(2))

# index
print(t.index(2))

# len

print(len(t))

# min
print(min(t))

#max
print(max(t))

# sum
print(sum(t))

#sorted
print(sorted(t))

# type
print(type(t))

#index
t = ("a", "b", "c")
print(t[0])
print(t[-1])

#slice
t = (1, 2, 3, 4, 5)
print(t[1:4])

# concat

t = (1, 2, 3)
t2 = ("a", "b", "C")
t3 = t + t2
print(t3)

#member
t = (1, 2, 3)
print(2 in t)

# uniqueness
t = (1, 2, 3, 4, 5)
print(len(set(t)))

#convert to list
t = (1, 2, 3, 4, 5)
print(list(t))


# iterate witth a for loop

my_set = {"alice", "bob", "charlie"}
for item in my_set:
    print(item)

# convert
my_set = {1, 2, 3, 4, 5}
my_list = sorted(my_set)
print(my_list[2])

#unpark
my_set = (1, 2, 3, 4, 5) 
a, b, c, d, e = my_set
print(a, b, c, d, e)

score = int(input("enter your score:"))

if score >= 90:
    print(f"grade A")

elif score >=80:
    print(f"grade B")

elif score >= 70:
    print(f"grade B")

elif score >= 60:
    print(f"grade C")

else:
    print(f"grade F")


