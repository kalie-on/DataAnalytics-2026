try:

    # Ask the user for a number
    number = int(input("Enter a number: "))

    # Divide 100 by the number
    result = 100 / number

except ValueError:
    # Runs if the user enters non-numeric data
    print("Error: Please enter a valid number.")

except ZeroDivisionError:
    # Runs if the user enters 0
    print("Error: Cannot divide by zero.")

else:
    # Runs only if no errors occur
    print(f"The result is: {result}")

finally:
    # Always runs whether an error occurs or not
    print("Program execution completed.")



class Car:
    pass

my_car = Car()