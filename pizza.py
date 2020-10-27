pizzas = ['tikka', 'suasage', 'meaty']
for pizza  in pizzas:

	print(pizza +'\n')
	print("I like, " + pizza.title() + " pizza. \n" )

print('I really love pizza!')

friend_pizzas = pizzas[:]

pizzas.append('tomato')
friend_pizzas.append('olive')

print("\nMy favourite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend favourite pizzas are")
for pizza in friend_pizzas:
	print(pizza)
