def greeting(name, city, hobby):
    return name, city, hobby


result = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)

print(type(result))

print(f"Hello, {result[0]}! You are from {result[1]} and you enjoy {result[2]}.")



def give():
    name = "Ndifon Caleb"
    return name

result = give()

print(f"Hello, {result}!")


# 1. Creating a string
text = "Python"

# 2. Indexing (positive and negative)
print("First character:", text[0])      # 'P'
print("Last character:", text[-1])      # 'n'

# 3. Slicing
print("First three characters:", text[0:3])   # 'Pyt'
print("From index 2 to end:", text[2:])       # 'thon'
print("Every second character:", text[::2])   # 'Pto'

# 4. Iteration
print("Characters in string:")
for char in text:
    print(char, end=" ")
print()

# 5. Membership testing
print("'Py' in text?", "Py" in text)        # True
print("'Java' in text?", "Java" in text)    # False

# 6. Length of string
print("Length of string:", len(text))       # 6

# 7. Concatenation and repetition
print("Concatenation:", text + "3.11")      # 'Python3.11'
print("Repetition:", text * 2)              # 'PythonPython'

# 8. Immutability demonstration
try:
    text[0] = "J"   # This will raise an error
except TypeError as e:
    print("Strings are immutable:", e)




def split_name(full_name):
    parts = full_name.split()
    return parts


result = split_name("Ndifon Caleb Ndakina")

print(result)