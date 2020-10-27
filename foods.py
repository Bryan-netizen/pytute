my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print('My favourite foods are:')
print(my_foods)

print("\nMy friends favourite foods are:")
print(friends_foods)


print("\nI like:")
for food in my_foods:
	print(food)

print("\nMy friends like:")
for food in friends_foods:
	print(food)