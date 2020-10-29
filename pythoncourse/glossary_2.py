glossary_2 = {'integer': 'numbers', 'strings': 'words',
              'operators': '+-/*', 'conditions': '> <', }

for name, defintion in glossary_2.items():
    print("\n" + name.upper() + ": " + defintion.title())


rivers = {'nile': 'egypt', 'amazon': 'brazil', 'thames': 'uk', }

for river, country in rivers.items():
    print("\nThe " + river.title() + " runs through " + country.title() + ".")

for key in rivers.keys():
    print(key.title())

for value in rivers.values():
    print("\n" + value.title())
