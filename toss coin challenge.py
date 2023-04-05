import random

def toss():
	if random.randint(0,1) == 0:
		return 'heads'
	else:
		return 'tails'

flip_count = 0

for trial in range(10_000):
	
	flip_count += 1
	flip_1 = toss()
	flip_count += 1
	
	while toss() == flip_1:
		flip_count += 1
	else:	
		continue

flip_avg = flip_count / 10_000

print(flip_avg)	
	

	

