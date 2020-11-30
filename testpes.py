
import random


better_pay=[]
beg = 700
end = 10000

for i in range (1000):
	random.seed(2)
	better_pay.append(random.randint(beg, end))

print(better_pay)