import random                                           #not the oop version
class Birthday:
    #First we're going to specify the number of experiments
    trials =  10000

    #make a loop for the number of people (5, 10, 15... 100) + this loop initializes the birthday matches from 0 to (if a match is found then +1)--> (then if another match is found then +2)
    # so in this way we're going to get the number of matches/duplicates then use them in our probablity variable.  


    for n in range(5, 105, 5):
        matches = 0 

    #make a nested loop in which we're going to increment our matches (if found) + make the system assign a random birthday to a person
        
        for t in range(trials):       #it's going to loop itself 10,000 times as it is going to be the no of experiments
            birthdays = [random.randint(1, 365) for _ in range(n)]   #we used "_" except i/j because we need to tell the system that the value of n/trials is not useful, but we need it to form a loop.
            
            if len(birthdays) != len(set(birthdays)):
                matches+= 1 
                """ if t== 0:
                    seen = set()
                    for b in birthdays:   #this is solely if we want the duplicates IN the FIRST exp(extra)
                        if b in seen:
                            print(f"Duplicate found: {b}")
                        else:
                            seen.add(b)
 """
        probability = matches / trials 
        print (f"Within {n} people, the probaility of getting the same birthdays is {probability}")
