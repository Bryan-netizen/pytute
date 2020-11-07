def make_shirt(size, message):
    """Accepts size and message printed on shirt."""
    print("\nThis shirt is size: " + size +
          " and says, " + message.upper() + ".")


make_shirt('21', 'hello')
make_shirt(size='22', message="hello again")


def make_shirt(size, message='i love python'):
    """Accepts size only."""
    print("\nThis shirt is size " + size +
          " and says, " + message.upper() + ".")


make_shirt(size='11')

make_shirt(size='large')

make_shirt(size='medium')
make_shirt(size='small', message='I still love python')
