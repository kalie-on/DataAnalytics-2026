bank_balance = 200
savings_goal = 1000
weekly_savings = 150

while bank_balance < savings_goal:

    bank_balance = bank_balance + weekly_savings

    if bank_balance >= savings_goal * 0.75:
        bank_balance = bank_balance - 25
        print("So close! After treating myself, my balance is up to $", bank_balance)

    elif bank_balance >= savings_goal / 2:
        print("Almost there! This week my balance is up to $", bank_balance)

    else:
        print("This week my balance increased to $", bank_balance)

print("Goal met! My current balance is $", bank_balance)