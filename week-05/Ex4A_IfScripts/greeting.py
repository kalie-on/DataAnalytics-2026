
time = int(input("enter time from 0 - 23:"))

if time <= 4 or time >= 23:
    print(" what are you doing up so late")

elif time < 10:
    print("good morning!")

elif time < 17:
    print("good day")

else:
    print("good evining")
