import matplotlib.pyplot as plt

# 1.  Allocate an array of 100,000 elements,
# one element to contain and track every square inch of the yard.
# 2.  Set the initial state of the yard to susceptible to weeds.
# 3.  Initialize the yard with a certain number of weeds, say 10.
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
# 5.  Plot the resulting number of weed infestations per day.
