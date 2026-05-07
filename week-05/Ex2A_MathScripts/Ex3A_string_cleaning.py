name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# convert to lowercase

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# convert to title case

print(name_1.title())
print(name_2.title())
print(name_3.title())

salary_1 = salary_1.replace("$", "")
salary_2 = salary_2.replace("$", "")

print(salary_1)
print(salary_2)

print(type(salary_1))
print(type(salary_2))

salary_1_int = int(
    salary_1.replace("$", "").replace(",", "")
)

print(salary_1_int)
print(type(salary_1_int))