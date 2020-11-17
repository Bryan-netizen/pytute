banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# if loop validating user not in banned_users list.


banned_users_2 = ['john', 'smith', 'judas']
user_2 = 'simon'
if user_2 not in banned_users_2:
    print(user_2.title() + " is a good man.")

banned_users_3 = ['james', 'johana', 'eve']
user_3 = 'eve'
if user_3 in banned_users_3:
    print(user_3.title() + " i just knew.")


# in and not in validating one user from a list, i think it can only check one item against he list.

# edit:
# python does not have  a switch case, cannot validate two items.
