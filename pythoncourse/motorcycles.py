motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append('honda')

print(motorcycles)

motorcycles.insert(0, 'ducati_2')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ["honda", "yamaha", "suzuki"]
last_owned  = motorcycles.pop()
first_owned = motorcycles.pop(0).title()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
print("The first motorcycle I owned was a " + first_owned + ".")


motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
motorcycles.remove("suzuki")
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(motorcycles)

print("\nA " + too_expensive.title() + " is too expensive for me.")
