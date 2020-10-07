# this program says hello and my name

print('Hello world')
print('What is your name?')  # ask for their name

myName = input()
print('Its is good to meet you, ' + myName)

print('The length of your name is :')
print(len(myName))

print('What is your age?')  # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


print("test this")


42 == 42
42 == " hello "

# integers and string will never equal to each other

myAge = 24
myPet = 'cat'
myAge > 20 and myPet == 'cat'