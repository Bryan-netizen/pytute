filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("\n" + str(123))

with open(filename, 'a') as file_object:
	file_object.write("\nI also love finding meaning in large datasets.")
