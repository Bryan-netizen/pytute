courses = ['History', 'Math', 'Physics', 'CompSci']
courses2= ['Art', 'Education']
nums = [1, 5, 2, 4, 3]


courses.append ('Art')

courses.insert(0, 'Geo')

courses.insert(0, courses2)

print(courses[0:2]) # Prints from 0 to 1 but not including 2

print(courses[2:]) #assumes all the way to the end Also known a sclicing

courses.extend(courses2)
print(courses)


courses.remove('Math')

print(courses)

popped = courses.pop() # removes last item in list

print(popped)


courses.reverse()

courses.sort()

print(courses)


print(nums)


nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)


sorted_courses = sorted(courses) 
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('CompSci'))

print('Art' in courses)
print('Math' in courses)


for item in courses:
	print(item)

for index, course in enumerate(courses , start=1):
	print(index, course)

courses = ['History', 'Math', 'Physics', 'CompSci']

course_str = ', '.join(courses)

print(course_str)

new_list = course_str.split(' - ')
print(new_list)
