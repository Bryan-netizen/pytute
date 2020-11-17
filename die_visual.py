from die import Die
import pygal

# Create a D6.

die = Die()

# Make some rolls, and store results is a list.
results = []

for roll_num in range(10000):
    result = die.roll()
    results.append(result)
print(results)


# Analyze the results.
frequencies = []
# plus one adds the sides from position side 1 = 0 + 1, 2 = 1+1 etc till 6.
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


# Vizualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one 6 sided dice 10000 times."

hist.x_labels = ['1', '2', '3', '4', '5', '6']

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
