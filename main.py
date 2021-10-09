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

# what is C?
C = 0.3
# infested = C ^ 14
# I_tomorrow = R_0 * min(I_today * C, S_today)

# TODO: what is R_0 ?
r_naught = 0.3

infested_count = [weeds]

# 4.  Repeat until either there are no more weeds, or there is no more yard:
while weeds > 0 and grasses > 0:
    # 	A.  Compute the number of good grass that would be exposed to the weeds,
    #   exposed = C ^ 14
    exposed = weeds * (int)(C ** 14)

    # 	B.  Find the amount of un-infested lawn left.
    #   ALREADY DONE

    # 	C.  Find the number of possible infestations,
    # 	New_Exposures = min( { A, B } ).
    new_exposures = min(exposed, grasses)

    # 	D.  Allocate  New_Exposures’s worth of random numbers in the range of [0, 1].
    # 		If each random number is under $R_{0}$, then:
    # 			these square inches become infested
    # 		else :
    # 			these square inches remain susceptible.
    # 		For each new infested square inch:
    # 			i.   Record the day that this square inch became infested.
    # 			ii.  Mark this lawn sample as infested.
    random_numbers = [random.uniform(0, 1) for i in range(new_exposures)]
    # number of random numbers less than R_0
    new_infested = len(list(filter(lambda n: n < r_naught, random_numbers)))

    # 	E.  For all samples that have been infested more then 14 days,
    # 	mark this sample of the lawn as ruined.

    weeds -= infested[DURATION - 1]
    # new weeds
    weeds += new_infested
    grasses -= new_infested
    for i in range(DURATION - 1, 0, -1):
        infested[i] = infested[i - 1]
    infested[0] = new_infested

    infested_count.append(new_infested)

# key,value pairs of day and number of weeds
print(infested_count)

# 5.  Plot the resulting number of weed infestations per day.

plt.ylabel('Number of Infected')
plt.xlabel('Days')
plt.plot(infested_count)
plt.show()
