import random

def roll():
    fair_die = random.randint(1,6)
    return fair_die

total = 0

for trial in range(10_000):
    total = total + roll()

avg_roll = total / 10_000

print(f"The average result of 10_000 rolls is {avg_roll}")
        
