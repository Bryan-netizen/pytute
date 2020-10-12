# Mutable list, changing one list changes the other list.
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

list_2[0] = 'Chem'

print(list_1)
print(list_2)

# Immutable ,Tuples are immutable

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')

tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# Sets Order changes with execution - Mostly used for testing

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', "Art", "Design"}

print(cs_courses)

# This returns the itens similar in 2 lists
print(cs_courses.intersection(art_courses))

# This returns the courses that are not in art_courses
print(cs_courses.difference(art_courses))

print(cs_courses.union(art_courses))  # This returns both courses


# Empty Lists

empty_List = []
empty_List = list()

# Empty Tuples

empty_tuple = ()
empty_tuple = tuple()

# Empty Sets

empty_set = {} 	# This isn't right! it's a dict

empty_set = set()
