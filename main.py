import matplotlib.pyplot as plt
import random

DURATION = 14


def simulate(r_naught, c):
    # 1.  Allocate an array of 100,000 elements,
    # one element to contain and track every square inch of the yard.
    # 2.  Set the initial state of the yard to susceptible to weeds.
    # 3.  Initialize the yard with a certain number of weeds, say 10.

    weeds = 10
    grasses = 100000 - weeds

    # dictionary of length DURATION
    # infested[2] = number of weeds that have been alive (?) for 3 days
    infested = {}
    for i in range(DURATION):
        infested[i] = 0
    infested[0] = weeds

    infested_count = [weeds]

    # 4.  Repeat until either there are no more weeds, or there is no more yard:
    while weeds > 0 and grasses > 0:
        # 	A.  Compute the number of good grass that would be exposed to the weeds,
        exposed = weeds * c

        # 	B.  Find the amount of un-infested lawn left.
        #   ALREADY DONE: grasses

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

    # 5.  Plot the resulting number of weed infestations per day.
    plt.plot(infested_count)


simulate(0.3, 4.0)
simulate(0.3, 2.0)
simulate(0.3, 1.0)
simulate(0.3, 0.5)
simulate(0.3, 0.4)
simulate(0.3, 0.3)

plt.ylabel('Number of Infected')
plt.xlabel('Days')
plt.margins(0)
plt.show()
