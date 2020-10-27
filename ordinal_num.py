numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
	if num  < 2:
		print( str(num) + ' st')
	if num == 2:
		print(str(num) + ' nd')
	if num == 3:
		print(str(num)+ ' rd')
	if num >= 4 :
		print(str(num)+ ' th')
else:
	if num > 10:
		print( str(num) + " ")