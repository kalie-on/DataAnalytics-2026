candies = ("lollipop", "gummy bear", "jelly bean")
flavors = ("mango", "strawberry", "pineapple")

candy_combinations = set()

candy_combinations.add(candies[0] + " " + flavors[2])
candy_combinations.add(candies[1] + " " + flavors[1])
candy_combinations.add(candies[2] + " " + flavors[0])

print("Today's candy options include:")
print(candy_combinations)

# it prints in diffirint order. Sets do not always print in the same order