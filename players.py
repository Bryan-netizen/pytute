players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3:])


print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())


print("\nThe first three items in the list are:")
print(players[0:3])

print("\nThree items from the middle of the list are:")
print(players[1:4])

print("\nThe last three items in the last are:")
print(players[-3:])

