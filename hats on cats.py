# populating the dictionary 

hundred_cats = {}

for i in range(1,101):
    hundred_cats[i] = False

print(hundred_cats)

# round 1: stop at every cat, placing a hat on each on
# round 2: you stop only at every second cat
# round 3: stop only at every third cat
# etc.. till 100th round


cats_with_hats = []

for i in range(1,101):
    for cat in hundred_cats:
        if cat % i == 0:
            if hundred_cats[cat] == False:
                hundred_cats[cat] = True
            else:
                hundred_cats[cat] = False
        
for cat in hundred_cats:
    if hundred_cats[cat] == True:        
       cats_with_hats.append(cat)             
    

print("Summary after 100 rounds")
print(cats_with_hats)





