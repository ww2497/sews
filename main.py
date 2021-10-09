import matplotlib.pyplot as plt
import random

# 1.  Allocate an array of 100,000 elements,
# one element to contain and track every square inch of the yard.
# 2.  Set the initial state of the yard to susceptible to weeds.
# 3.  Initialize the yard with a certain number of weeds, say 10.

weeds = 10
grasses = 100000 - weeds

DURATION = 14
# dictionary of length DURATION
# infested[2] = number of weeds that have been alive (?) for 3 days
infested = {}
for i in range(DURATION):
    infested[i] = 0
infested[0] = weeds

# 4.  Repeat until either there are no more weeds, or there is no more yard:
# 	A.  Compute the number of good grass that would be exposed to the weeds,
# 	based on the cross-contamination rate.
# 	B.  Find the amount of un-infested lawn left.
# 	C.  Find the number of possible infestations,
# 	New_Exposures = min( { A, B } ).
# 	D.  Allocate  New_Exposures’s worth of random numbers in the range of [0, 1].
# 		If each random number is under $R_{0}$, then:
# 			these square inches become infested
# 		else :
# 			these square inches remain susceptible.
# 		For each new infested square inch:
# 			i.   Record the day that this square inch became infested.
# 			ii.  Mark this lawn sample as infested.
# 	E.  For all samples that have been infested more then 14 days,
# 	mark this sample of the lawn as ruined.

# what is C?
C = 1.1
# infested = C ^ 14
# I_tomorrow = R_0 * min(I_today * C, S_today)

# TODO: what is R_0 ?
r_naught = 0.9

day = 1
while weeds > 0 and grasses > 0 and day <= DURATION:
    # A. exposed = C ^ 14
    exposed = (int)(C ** 14)

    # B. uninfested = grasses

    # C.
    new_exposures = min(exposed, grasses)

    # D.
    random_numbers = [random.uniform(0, 1) for i in range(new_exposures)]

    # number of random numbers less than R_0
    new_infested = len(list(filter(lambda n: n < r_naught, random_numbers)))

    # update
    weeds += new_infested
    grasses -= new_infested

    # record the day this square inch became infested
    infested[day] = weeds

    # increment day
    day += 1

# key,value pairs of day and number of weeds
print(infested)

"""
while weeds > 0 and not grasses == 0:
    # A.

    # B.
    
    # C.
    new_exposures = ...
    
    # D.
    infestations = ...
    
    # E.
    weeds -= infested[DURATION - 1]     # ruined
    # new weeds
    weeds += infestations
    grasses -= infestations
    for i in range(DURATION - 1, 0, -1):
        infested[i] = infested[i - 1]
    infested[0] = new_exposures
    
"""

# 5.  Plot the resulting number of weed infestations per day.

# plt.ylabel('Number of Infected')
# plt.xlabel('Days')
# plt.show()
