def describe_city(city, country='germany'):
    """City and Country."""
    print("\n" + city.title() + " is in " + country.title() + ".")


describe_city('"nairobi"', 'kenya')

describe_city(city='tokyo', country='japan')

describe_city('capetown', 'south africa')
describe_city('munich')
