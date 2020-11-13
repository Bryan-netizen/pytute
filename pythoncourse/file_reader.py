with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())


filename = 'pi_digits.txt'

print("\n")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


with open(filename) as file_object:
    lines = file_object.readlines()

print("\n")
for line in lines:
    if line == float(2643383279):
        print(line.rstrip())

print("\n")


# file_path = '/home/sibs/Documents/pytute/pythoncourse/pi_digits.txt'

# with open(file_path) as file_object:
# contents = file_object.read()
# print(contents.rstrip())

# with open('/home/sibs/Documents/pytute/pythoncourse/pi_digits.txt') as file_object:
#   contents = file_object.read()
#  print(contents.rstrip())
