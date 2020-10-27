for value in range(1,6):
	print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares= []
for value in range(1,11):
	squares.append(value**2)
	print(squares)


digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))



squares = [value**2 for value in range(1,11)]
print(squares)

twenty = [value for value in range(1,21)]
print(twenty)

#million = [value for value in range(1,1_000_000)]
#print(million)

#million = list(range(1,1_000_001))
#print(million)
#print(min(million))
#print(max(million))
#print(sum(million))


#print(million)


for odd_numbers in list(range(1,21,2)):
	print(odd_numbers)

for multiples_of_three in range(3,31,3):
	print(multiples_of_three)


cube_list = [value**3 for value in list(range(1,11))]
print(cube_list)

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the
#first 10 cubes.
