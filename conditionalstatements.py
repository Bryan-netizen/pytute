
# Comparisons:
# Equal:			==
# Not Equal: 		!=
# Greater Than:	 	>
# Less Than:	 	<
# Greater or Equal: >=
# Less or Equal:	<=
# Object Identity:	is

if True:
	print('Condition was True')

if False:
	print('Condition False')

language = 'Java' # python does not have  a switch case, cannot validate two items


if language == 'python':
	print('language is python')
elif language == 'Java':
	print('language is Java')
elif language == 'JavaScript':
	print('language is JavaScript')
else:
	print('no match')


# and
# or
# not

user = 'Admin'
logged_in = False #True False statements do not need ''

if user == 'Admin' and logged_in:
	print('Admin page')
else:
	print('Bad Creds')

if not logged_in:
	print('Please logged in')
else:
	print('Welcome')




# False Values: Conditions that alwasy evaluate to False

# False
# None
# Zero of any numeric type
# Any empty sequence, For example, '', (), [].
# Any empty mapping. For example, {}.

Condition = False

if Condition:
	print('evaluated to True')
else:
	print('evaluated to False')

Condition2= None

if Condition2:
	print('evaluated to true')
else:
	print('evaluated to False')

Condition3 = 0

if Condition3:
	print('evaluated to True')
else:
	print('evaluated to False')

Condition4 = ''

if Condition4:
	print('evaluated to True')

else:
	print('evaluated to False')
