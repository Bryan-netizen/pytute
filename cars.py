cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# this alphabetically sorts list.


cars.sort(reverse=True)
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here	is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

# Past tense sorting when printing.

print("\nHere is the original list again:")
print(cars)

print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))


print(cars)

cars.reverse()
print(cars)

print(len(cars))


for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("Is car =='subaru'?I predict False")
print(car == 'subaru'.title())


print("is car == 'subaru'? I predict False")
print(car == 'subaru'.upper())

car_len = len('subaru')

print(car_len)

print("Is car_len > 7? I predict False")
print(len(car) > car_len)

print("Is car_len == 6? I predict True")
print(len(car) >= car_len)

print("Is car_len != 6? I predict False")
print(len(car) != car_len)

print('subaru' in cars)

print('subaru'.title() in cars)
