toppings_prompt = ("\n Add a toping to your pizza: ")
toppings_prompt += ("\n Enter 'done' when done adding toppings. ")

while True:
    toppings = input(toppings_prompt)

    if toppings == 'done':
        print("\nToppings are all added!")

        break
    else:
        print("\n" + toppings.title() + " added!")
        continue
