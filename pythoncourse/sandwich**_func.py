def sandwich_filling(*fillings):
    """List of fillings."""
    print('\nHere are the fillings in the sandwich.')
    for filling in fillings:
        print("- " + filling.title())


sandwich_filling('ham')

sandwich_filling('green peppers')

sandwich_filling('bacon', 'eggs', 'cheese')
