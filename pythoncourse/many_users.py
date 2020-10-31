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

    print("\nFull name: " + full_name.title())
    print("\tLocation: " + location.title())


futurama = {
    'fry': {
        'species': 'human',
        'location': 'future',
    },
    'bender': {
        'species': 'robot',
        'location': 'earth',
    },
    'nibbler': {
        'species': 'alien',
        'location': 'deep space',

    },
}

for username, users_info in futurama.items():
    print("\n username " + username.title() + ".")
    location = users_info['location']
    print("location: " + location.title() + ".")


cities = {
    'nairobi': {
        'country': 'kenya',
        'fact': 'the only city with a national park in it',
    },
    'tokyo': {
        'country': 'japan',
        'fact': 'the most populous city in the world',
    },
    'cairo': {
        'country': 'egpyt',
        'fact': 'a city kept alive by the nile',
    },
}

for city, info in cities.items():
    location = info['country']
    fact = info['fact']
    print("\n" + city.title() + ", is located in " +
          location.title() + ", it is " + fact + ".")


numbers = {
    'jen': {
        'fav_num_1': 5,
        'fav_num_2': 6,
        'fav_num_3': 1,
    },
    'john': {
        'fav_num_1': 8,
        'fav_num_2': 3,
        'fav_num_3': 1,
    },
    'smith': {
        'fav_num_1': 1,
        'fav_num_2': 0,
        'fav_num_3': 2,
    },
}

for name, info in numbers.items(): 
    favourite = info['fav_num_1']
    favourite_2 = info['fav_num_2']
    favourite_3 = info['fav_num_3']
    print("\n" + name.title() + " favourite numbers are, " + str(favourite) + ","
          + str(favourite_2) + "," +str(favourite_3) + ".")
