student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']} # These are keys

student['phone'] = '555-5555'

student.update({'name':'Jane', 'age': 26, 'phone': '123-1234'})

print(student['name'])
print(student.get('name'))

print(student.get('phone', 'Not Found'))

print(student)

#del student['age']
print(student)

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']} # These are keys

#age = student.pop('age')
#print(student)
#print(age)

#print(len(student))
#print(student.keys())
#print(student.values())
#print(student.items())

for key, value in student.items():
	print(key,  value)