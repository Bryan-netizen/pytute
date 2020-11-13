from car_class import Car
"""Car module."""

my_newest_car = Car('audi', 'a4', 2016)
print(my_newest_car.get_descriptive_name())

my_newest_car.odometer_reading = 23
my_newest_car.read_odometer()
