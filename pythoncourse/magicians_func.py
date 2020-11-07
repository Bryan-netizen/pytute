magicians = ['jesus', 'deming', 'putin']


def show_magicians(magicians):
    """Print the list of magicians."""
    for magician in magicians:
        print(magician)


show_magicians(magicians)


def make_great(magicians):
    """Modify print magician with great."""
    for magician in magicians:
        print("\nGreat " + magician.title())


make_great(magicians[:])


great_magicians = make_great(magicians[:])

show_magicians(magicians)
show_magicians(great_magicians)
