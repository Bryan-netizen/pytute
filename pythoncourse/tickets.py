age = input("Enter age to see price: ")
age = int(age)

if age <= 3:
    print("\nTicket cost FREE")
elif age in range(3, 12):
    print("\nTicket cost $10")
elif age > 12:
    print("\nTicket cost $15")

else:
    if age != age:
        print("\n You have not entered a digit, please try again.")
