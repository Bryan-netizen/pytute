print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot')
    elif int(numCats) <= 0:
        print('You testing me')
    else:
        print('not enough yet')
except ValueError:
    print('You did not enter a number')

# validtes input numCats against comparison  and prints statements,
# except valueerror to make sure int is entered.