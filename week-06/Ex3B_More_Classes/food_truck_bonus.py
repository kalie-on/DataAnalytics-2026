class Restaurant:

    def __init__(self, rest_name, food_type):

        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):

        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):

        print(f"{self.rest_name} is open.")

class FoodTruck(Restaurant):
    '''This class represents a food truck.'''

    def __init__(self, rest_name, food_type):

        super().__init__(rest_name, food_type)

        self.private_bookings = "N"
        self.truck_location = ""

        self.location_history = []

    def accepts_private_bookings(self):

        answer = input(
            "Does this food truck accept "
            "private bookings? Y/N "
        )

        self.private_bookings = answer.upper()

        if self.private_bookings == "Y":

            print(
                "This food truck currently "
                "accepts private bookings."
            )

        else:

            print(
                "This food truck currently "
                "does not accept private bookings."
            )

    def relocate_truck(self):

        location = input(
            "Enter current truck location: "
        )

        self.truck_location = location

        print(
            f"Truck is currently located at "
            f"{self.truck_location}"
        )

        # Add location to history
        # This version keeps duplicates so we can
        # track every stop the truck visits.
        self.location_history.append(location)

    # Print location history
    def show_location_history(self):

        print("Location History:")

        for location in self.location_history:

            print(location)


truck1 = FoodTruck(
    "Tasty Truck",
    "Street Food"
)


truck1.describe_rest()

truck1.rest_open()

truck1.accepts_private_bookings()

truck1.relocate_truck()

truck1.relocate_truck()

truck1.show_location_history()