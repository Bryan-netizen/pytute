favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


print("Sarah's favourite language is " +
      favourite_languages['sarah'].title() +
      ".")

person = {
    'first_name': 'man',
    'last_name': 'like',
    'city': 'nairobi',
}

print(person['first_name'].title() +
      " " + person['last_name'].title() +
      ", lives in " +
      person['city'].title() +
      ".")

favourite_numbers = {
    'john': '1',
    'tom': '2',
    'agnes': '3',
    'mary': '2',
    'james': '5',
}


print("John's favourite numbers is " +
      favourite_numbers['john'] +
      ", " +
      "& Tom's favourite numbers is " +
      favourite_numbers['tom'] +
      ".")


glossary = {'glossary': 'dictionary',
                        'tuples': 'immutable_list',
                        'list': 'mutable',
                        'string': 'word',
                        'integer': 'numbers', }


print("\n" + glossary['glossary'] +
      "\n" + glossary['list']
      )


print(favourite_languages)

for name, language in favourite_languages.items():
    print("\n" + name.title() +
          "'s favourite language is " +
          language.title() + ".")


friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() +
              ", I see your favourite language is " +
              favourite_languages[name].title() + "!")
    if 'erin' not in favourite_languages.keys():
        print("Erin please take our poll!")
    for name in sorted(favourite_languages.keys()):
        print(name.title() + ", thank you for taking the poll.")


print("\nThe following languages have been mentioned:")
for language in favourite_languages.values():
    print("\n" + language.title())

for language in set(favourite_languages.values()):
    print(language.title())


poll_friends = ['john', 'sarah', 'peter', 'meeps', 'phil', 'jen', ]

for name in poll_friends:
    if name in favourite_languages.keys():
        print("\n" + name.title() + ", Thank you for taking the poll.")
    if name not in favourite_languages.keys():
        print("\n" + name.title() + ", Please take the poll.")

popular_languages = ['c', 'javascript', 'python', 'c++', 'bash']

for language in popular_languages:
    if language in favourite_languages.values():
        print("\n" + language.title() + ", is a popular language!")
    if language not in favourite_languages.values():
        print("\n" + language.title() + ", is not a popular language.")


favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell', ]
}


for name, languages in favourite_languages.items():
    if languages in favourite_languages.values():
        print(len(language))
    print("\n" + name.title() + "'s favourite languages are:")
    for language in languages:
        print("\t" + "-" + language.title())