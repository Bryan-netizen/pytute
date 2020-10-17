name = "ada lovelace"
print(name.title())  	# name.title(()) is a method that acts on the stored value
print(name.lower())		# Good for storing data in similar format
print(name.upper())


first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name.title())
print("Hello, " + full_name.title() + "!")

print("python")

print("\tpython".title()) # inserting whitespace with \t for tab

print("languages:\npython\nC\njavascript".title()) # insert whitespcae with \n for new line

print("languages:\n\tpython\n\tC\n\tjavasript".title()) # insert whitespace with both \n\t


favourite_language = 'python '
print(favourite_language)
print(favourite_language.rstrip()) # this is a temporary storage of the stripped value
								   # to make it permanent you have to store it in a variable


favourite_language = favourite_language.rstrip()
print(favourite_language)								

fav_lang = '  Python '

fav_lang =  fav_lang.rstrip().lstrip().title()  # This works to apply multiple methods at the same time
print(fav_lang)
