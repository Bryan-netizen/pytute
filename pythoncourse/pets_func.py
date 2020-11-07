def describe_pet(animal_type, pet_name):
    """Display information about pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("hamster", "harry")
describe_pet("cat", 'meeps')


describe_pet(animal_type='hamster', pet_name='harry')


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name="willie")


# When you use default values, any parameter with a default value needs to be listed
# after all the parameters that don’t have default values.
# This allows Python to continue interpreting positional arguments correctly.
