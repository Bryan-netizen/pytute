cities = ["Nairobi", "Capetown", "Cairo", "Tokyo", "Berlin", "London","Rome"]

cities_lower = [x.lower() for x in cities]
print(cities_lower)


print(sorted(cities_lower))

print(cities_lower)

print(sorted(cities_lower, reverse=True))

print(cities_lower)

cities_lower.reverse()

print(cities_lower)

cities_lower.reverse()
print(cities_lower)

cities_lower.sort()
print(cities_lower)

cities_lower.sort(reverse = True)
print(cities_lower)


print(len(cities_lower))

cities_lower.append("Paris")
cities_lower = [x.lower() for x in cities_lower]

print(cities_lower)
print(len(cities_lower))
cities_lower.insert(-1, "kampala")

print(cities_lower)

cities_lower_popped=cities_lower.pop()

print(cities_lower_popped)

print("I have never been to, " + cities_lower_popped + ".")
print("I have never been to, " + cities_lower_popped + ".")

del cities_lower[-1]
del cities_lower[-1]
print(cities_lower) 