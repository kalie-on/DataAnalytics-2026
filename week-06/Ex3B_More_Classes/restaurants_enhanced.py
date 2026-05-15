class Restaurant:

    def __init__(self, rest_name, food_type):

        self.rest_name = rest_name
        self.food_type = food_type

        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):

        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):

        print(f"{self.rest_name} is open.")

    def add_num_served(self):

        customers = int(input("How many customers served today? "))

        self.number_served += customers

    def print_num_served(self):

        print(
            f"{self.rest_name} has served "
            f"{self.number_served} customers"
        )

    def customer_rating(self):

        rating = input("Rate 1-5: ")

        if rating.isdigit():

            rating = int(rating)

            if 1 <= rating <= 5:

                self.customer_ratings.append(rating)

                average = (
                    sum(self.customer_ratings)
                    / len(self.customer_ratings)
                )

                print(
                    f"Your rating was {rating}. "
                    f"Average rating is {average:.2f}"
                )

            else:

                print("Enter a number from 1-5.")

        else:

            print("Invalid input.")


restaurant1 = Restaurant(
    "Mama's Kitchen",
    "African food"
)

restaurant2 = Restaurant(
    "Pizza Palace",
    "Italian food"
)

restaurant3 = Restaurant(
    "Sushi World",
    "Japanese food"
)


restaurant1.print_num_served()

restaurant1.add_num_served()

restaurant1.print_num_served()


restaurant1.customer_rating()

restaurant1.customer_rating()