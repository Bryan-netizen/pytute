sandwich_orders = ['tuna', 'salami', 'roastbeef', 'egg',
                   'pastrami', 'lamb', 'pastrami', 'goat', 'pastrami', ]

finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("We are out of Pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("\nI made your " + current_sandwich.title() + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print('\nThe following sandwiches have been made: ')

for sandwich in finished_sandwiches:
    print(sandwich.title())
