def display_mailing_label(name, address, city, state, zip):

    print(name)
    print(address)
    print(f"{city}, {state} {zip}")

display_mailing_label(
    "ndifon caleb",
    "123 Main Street",
    "wilmington",
    "DE",
    "19725"
)

def add_numbers(*numbers):

    total = sum(numbers)

    expression = " + ".join(str(num) for num in numbers)

    print(f"{expression} = {total}")

add_numbers(5)

add_numbers(3, 7)

add_numbers(1, 2, 3, 4, 5) 

def display_receipt(total_due, amount_paid):

    change = amount_paid - total_due

    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if amount_paid > total_due:

        print(f"Change Due: ${change:.2f}")

    elif amount_paid == total_due:

        print("Bill paid exactly.")

    else:

        balance = total_due - amount_paid

        print(f"Remaining Balance: ${balance:.2f}")


display_receipt(50, 60)

display_receipt(40, 40)

display_receipt(75, 50)