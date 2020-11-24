import csv

from matplotlib import pyplot as plt

filename = '/home/sibs/Documents/resources/chapter_16/sitka_weather_07-2014.csv'


with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	#print(header_row)

#for index, column_header in enumerate(header_row):

#	print(index, column_header)

# Get high temperatures from_file

	highs = []

	for row in reader:			# improper indentation will give I/O value error on closed file.
		high = int(row[1])
		highs.append(high)
	print(highs)

	# Plot data.
	fig = plt.figure(dpi = 128, figsize=(10,6))
	plt.plot(highs, c = 'red')
	
#Format plot.
	plt.title("Daily high temperatures, July 2014", fontsize=24)
	plt.xlabel('',fontsize=16)
	plt.ylabel("Temperatures (F)", fontsize=16)
	plt.tick_params(axis='both',which='major', labelsize=16)

	plt.show()