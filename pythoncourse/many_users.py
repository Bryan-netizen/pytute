users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

}


for username, users_info in users.items():
    print("\nUsername: " + username)
    full_name = users_info['first'] + " " + users_info['last']
    location = users_info['location']

    print("\nFull name:" + full_name.title())
    print("\tLocation:" + location.title())
