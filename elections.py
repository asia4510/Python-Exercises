import random

probability = [0.87, 0.65, 0.17]

num_of_elections = 10_000

def election(x):
    if random.random() < x:
        return 1
    else:
        return 0

win_A = 0
win_B = 0

for trial in range(num_of_elections):

    vote_for_A = 0
    vote_for_B = 0

    for i in probability:
        if election(i) == 1:
            vote_for_A = vote_for_A + 1
        else:
            vote_for_B = vote_for_B + 1

    if vote_for_A > vote_for_B:
        win_A = win_A + 1
    else:
        win_B = win_B + 1

print(f"Candidate A wins in {win_A/100}% of times")




        
    
    
