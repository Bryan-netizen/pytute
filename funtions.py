def hello_func(greeting, name = 'You'):
	return '{}, {}'.format(greeting, name)

print(hello_func('Hi', name = 'Bryan'))



def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)


# """This is a doc string. Used for documentation """
