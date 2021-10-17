import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import random
from collections import deque

# total duration in days
DURATION = 14
YARD_SIZE = 100000

def simulate(r_naught, c):
    # 1.  Allocate an array of 100,000 elements,
    # one element to contain and track every square inch of the yard.
    # 2.  Set the initial state of the yard to susceptible to weeds.
    # 3.  Initialize the yard with a certain number of weeds, say 10.

    weeds = 10
    grasses = YARD_SIZE - weeds

    # queue of size DURATION
    # first element = number of weeds that have been alive (?) for DURATION (14) days
    infested = deque()
    for _ in range(DURATION - 1):
        infested.append(0)
    infested.append(weeds)

    active_weeds = [weeds]

    # 4.  Repeat until either there are no more weeds, or there is no more yard:
    while weeds > 0 and grasses > 0:
        # 	A.  Compute the number of good grass that would be exposed to the weeds,
        exposed = (int)(weeds * c)

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
        weeds -= infested.popleft()

        # new weeds
        weeds += new_infested
        grasses -= new_infested

        infested.append(new_infested)
        active_weeds.append(weeds)

    # 5.  Plot the resulting number of actively growing weeds per day.
    # label for legend
    lbl = "$R_0 = {0}, c = {1}$".format(r_naught, c)
    plt.plot(active_weeds, label=lbl)

# scale figure nicely
figure(figsize=(8, 6), dpi=120)

# simulate each curve
simulate(0.3, 4.0)
simulate(0.3, 2.0)
simulate(0.3, 1.0)
simulate(0.3, 0.5)
simulate(0.3, 0.4)
simulate(0.3, 0.3)

plt.title('$R_0$ is The Viral Reproduction Number, C is #Contacts, Person to Person')
plt.ylabel('Actively Growing Weeds On Each Day (in thousands)')
plt.xlabel('Day')
# start plot at origin (0, 0)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
# show legend describing each curve
plt.legend(loc="upper right")
# save plot to a file and display it
plt.savefig('weed_spread.png')
plt.show()
