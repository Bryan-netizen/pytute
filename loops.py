nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print(str(num) + ' ##Found##!')
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)


for int in range(1, 10):
    print(int)

x = 0

while x < 10:
    if x == 5:
        break
        pass
    print(x)
    x += 1


while True:  # This is useful for searching for something as it runs until condition is met
    if x == 5:
        break
        print(x)
        x += 1
