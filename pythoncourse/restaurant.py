class Restaurant():
    """Name and cuisine type."""

    def __init__(self, restaurant_name, cuisine_type):
        """Name and type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Name and type of restaurant."""
        print("\nThe " + self.restaurant_name.title() + ", is a " +
              self.cuisine_type.title() + " restaurant.")

    def open_restaurant(self):
        """Indicate status of restaurant."""
        print(self.restaurant_name.title() + " is now open.")

    def restaurant(self):
        print(" This restaurant has served" + ", "
              + str(self.number_served) + " customers.")

    def update_restaurant(self, numbers):
        """Update the customers served."""
        self.number_served = numbers

    def increment_number_served(self, daily):
        """Adding daily number of customers."""
        self.number_served += daily


class IceCreamStand(Restaurant):
    """Ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """Restaurant class."""

    def ice_cream_flavors(self, flavors):
        """Ice cream flavours."""
        self.flavor = vanilla


my_ice_cream_stand = IceCreamStand('iceman', 'icecream')


my_restaurant = Restaurant('blue lagoon', 'japanese')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.restaurant()

old_restaurant = Restaurant("kibanda", "fast-food")

old_restaurant.describe_restaurant()
old_restaurant.open_restaurant()
old_restaurant.update_restaurant(100)
old_restaurant.restaurant()


new_restaurant = Restaurant("veggie", "vegeterian")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
new_restaurant.restaurant()
new_restaurant.update_restaurant(10)
new_restaurant.restaurant()
new_restaurant.increment_number_served(200)
new_restaurant.restaurant()
