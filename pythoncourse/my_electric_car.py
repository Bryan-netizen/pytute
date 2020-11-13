from car_class import ElectricCar

my_tesla3 = ElectricCar('tesla3', 'model s', 2016)

print(my_tesla3.get_descriptive_name())
my_tesla3.battery.describe_battery()
my_tesla3.battery.get_range()
