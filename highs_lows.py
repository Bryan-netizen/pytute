import csv

filename = '/home/sibs/Documents/resources/chapter_16/sitka_weather_07-2014.csv'


with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	#print(header_row)

for index, column_header in enumerate(header_row):
	print(index, column_header)

# Get high temperatures from_file

