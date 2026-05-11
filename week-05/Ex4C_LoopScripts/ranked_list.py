foods = ["Tacos", "Pizza", "Ramen", "Jerk Chicken", "Burger"]

for index, food in enumerate(foods, start=1):

    if index == 1:
        print(index, ".", food, "<- top pick!")
    else:
        print(index, ".", food)

print("\nReverse Order:\n")

reverse_foods = list(reversed(foods))

for index, food in enumerate(reverse_foods, start=1):
    print(index, ".", food)