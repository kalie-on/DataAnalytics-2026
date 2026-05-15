try:

    num = int("hello")

except ValueError:

    print("ValueError: Cannot convert text into a number." )

else:
    print(num)

finally:
    print("Let's try another one...")


# NameError

try:

    m = banana

except NameError:
    print("NameError: Variable is not defined.")

else:
    print(m)

finally:
    print("Let's try another one...")


# TypeError

try:

    result = "5" + 5

except TypeError:
    print("TypeError: Cannot add string and integer.")

else:
    print(result)

finally:
    print("Let's try another one...")


# SyntaxError example
# SyntaxError usually stops the whole script,
# so we simulate it using eval()


try:
    eval("if True print('Hello')")

except SyntaxError:

    print("SyntaxError: Invalid Python syntax.")

else:
    print("No syntax error.")

finally:
    print("Let's try another one...")
    