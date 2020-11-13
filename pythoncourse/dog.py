class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initailize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulates a dog sitting in response to command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()


print("\nMy dog's name is " + my_dog.name.title() + ".")
print("\nMy dog is " + str(my_dog.age) + " years old.")

your_dog = Dog('lucy', 3)
your_dog.sit()
your_dog.roll_over()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("\nYour dog is " + str(your_dog.age) + " years old.")
