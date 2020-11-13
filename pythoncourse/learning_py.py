with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

print("\n")

filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

print("\n")

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)


message = "I really like dogs."
message.replace('dogs', 'cats')
print(message.replace('dogs','cats'))
	