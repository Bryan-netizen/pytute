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
		" " + person['last_name'].title()+
		", lives in " + 
		person['city'].title()+ 
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
	favourite_numbers['tom']+
	".")



glossary = {'glossary': 'dictionary', 
			'tuples': 'immutable_list',
			'list': 'mutable',
			'string':'word',
			'integer':'numbers',}


print("\n" + glossary['glossary'] + 
	  "\n" + glossary['list']
	)