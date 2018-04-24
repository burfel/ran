''' COMPUTING: Assessed Exercise No. 2
	Felicia Burtscher
'''

'''

	DESCRIPTION:
		The following python script containing 2 functions to simulate 2 simple genetic drift models and visualises the results (see task Exercise No. 2):
		
		geneticDrift1():
		- Creates an initial population of size 100, half of which have allele "A" and half of which have allele "B".
		- Completes 1000 generations. 
		- Draws a plot of the allele frequencies of the whole course of generations; optionally you can choose a stacked histogram plot by using 
			geneticDrift1(histogram = True). If not wanted, comment it out in the code at the bottom!

		geneticDrift2():
		- Population size is 100, even distribution of alleles so 0.25 are "AA", 0.5 "Aa" (0.25 "Aa" and 0.25 "aA") and 0.25 "aa".
		- An evolutionary event has occurred, ie only 0.8 of "aa" individuals survive to maturity to breed.
			This is accomodated by accepting a drawn "aa" only in 0.8 of the cases to go into the new population.
		- With each generation one allele from a random individual should be combined with another allele (this could be the same, so self-mating is possible in our program) to create a new population of 100. 
		- Runs simulation for a maximum of 500 generations or until allele "aa" and "Aa"/"aA" (or "AA" and "Aa"/"aA") disappears from the population, at which point it should stop.
		- Draws a plot of the allele frequencies of the whole course of generations; optionally you can choose a stacked historgram plot by using 
			geneticDrift2(histogram = True). If not wanted, comment it out in the code at the bottom!

	INPUTS: 
		- [Only call "python ex2.py" in the respective directory]

	OUTPUTS: 
		Two plots:
		- One plot for geneticDrift1()
		- One plot for geneticDrift2()

	NOTE:
		The print functions in the following script can be ignored and are solely for debugging purposes.

'''


#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
import random as ran

def geneticDrift1(histogram = False):

# create an initial population of 50 "A" and 50 "B" alleles
	pop = ['A', 'B'] * 50
	gen_max = 1
	a_freq = [50]
	b_freq = [50]

	# up to 1000 generations or when either one was lost
	while gen_max <= 1000 and 'A' in pop and 'B' in pop:
		new_pop = [] # new list representing the new population
		# an allele from the current population is randomly selected and added to the new population;
		# this process is repeated 100 times (with replacement) in order to get the same length as the initial pupulation vector
		for i in range(100):
			new_pop.append(ran.choice(pop))
		# print("new population:", new_pop)
		# print("# generations left:", 1000-gen_max)
		a_freq.append(new_pop.count('A')) # store frequency of allele "A" in this generation
		b_freq.append(new_pop.count('B')) # store frequency of allele "B" in this generation
		# print("# A allele:", new_pop.count('A'))
		# print("# B allele:", new_pop.count('B'), '\n')
		pop = new_pop # the new population becomes the old population of the next round
		gen_max += 1

	# plot that shows the change in allele frequency with each generation
	if (histogram == False): 

		fig1 = plt.figure("Drift 1")
		line1, = plt.plot(range(0, gen_max), a_freq, 'r-', label="As")
		line2, = plt.plot(range(0, gen_max), b_freq, 'b-', label="Bs")
		plt.title('Frequency of allele types over the course of the generations')
		plt.ylabel('frequency of allele types')
		plt.xlabel('generations')
		legend1 = plt.legend(handles=[line1], loc=2)
		ax = plt.gca().add_artist(legend1)
		plt.legend(handles=[line2], loc=3)

		#plt.show()
		plt.draw()
		plt.pause(1) 
		input("<Hit Enter To Close>")
		plt.close(fig1)

	#histogram plot
	else: 

		fig2 = plt.figure("Drift 1")

		N = gen_max
		ind = np.arange(N)    
		width = 0.5       

		p1 = plt.bar(ind, a_freq, width, color='red')
		p2 = plt.bar(ind, b_freq, width, bottom=a_freq)

		plt.title('Frequency of allele types over the course of the generations')
		plt.ylabel('frequency of allele types')
		plt.xlabel('generations')
		plt.axis([0, gen_max, 0, 100])
		plt.legend((p1[0], p2[0]), ('A', 'B'))

		#plt.show()
		plt.draw()
		plt.pause(1) 
		input("<Hit Enter To Close>")
		plt.close(fig2)



def choose(pop):
	new_alleles = ran.choice(pop)
	if new_alleles == 'aa':
		if ran.uniform(0, 1) < 0.2:
			# print(new_alleles)
			new_alleles = choose(pop)
	return new_alleles


def geneticDrift2(histogram = False):

# create an initial population of 100; even distribution of alleles so 0.25 are "AA", 0.5 "Aa" (0.25 "Aa" and 0.25 "aA") and 0.25 "aa".
	pop = ['AA', 'Aa', 'aA', 'aa'] * 50
	gen_max = 0
	AA_freq = [25]
	Aa_freq = [50]
	aa_freq = [25]


	# simulation for a maximum of 500 generations or until allele "aa" and "Aa"/"aA" (or "AA" and "Aa"/"aA") disappears from the population
	while gen_max < 500 and ('aA' in pop or 'Aa' in pop or ('aa' in pop and 'AA' in pop)):
		which = [0, 1]
		new_pop2 = []
		for i in range(100):
			new_alleles1 = choose(pop)
			new_alleles2 = choose(pop) # self-mating/autofertilisation possible: we could draw the same item as before
			# print(new_alleles1, new_alleles2)
			new_alleles = new_alleles1[ran.choice(which)] + new_alleles2[ran.choice(which)]
			# print(new_alleles)
			new_pop2.append(new_alleles)
		AA_freq.append(new_pop2.count('AA'))
		Aa_freq.append(new_pop2.count('Aa') + new_pop2.count('aA'))
		aa_freq.append(new_pop2.count('aa'))
		# print("new population:", new_pop2)
		# print("# AA allele:", new_pop2.count('AA'))
		# print("# Aa allele:", new_pop2.count('Aa') + new_pop2.count('aA'))
		# print("# aa allele:", new_pop2.count('aa'))
		pop = new_pop2
		gen_max += 1
		# print("# generations left:", 500-gen_max, '\n')
		# print(AA_freq)
		# print(len(AA_freq))
		# print(len(Aa_freq))
		# print(len(aa_freq))


	# plot that shows the change in allele frequency with each generation
	if (histogram == False): 

		fig3 = plt.figure("Drift 2")
		line1, = plt.plot(range(0, gen_max+1), AA_freq, 'r-', label="AA")
		line2, = plt.plot(range(0, gen_max+1), Aa_freq, 'b-', label="Aa")
		line3, = plt.plot(range(0, gen_max+1), aa_freq, 'g-', label="aa")
		plt.title('Frequency of allele types over the course of the generations')
		plt.ylabel('frequency of allele types')
		plt.xlabel('generations')
		#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
		legend1 = plt.legend(handles=[line1], loc=2)
		ax = plt.gca().add_artist(legend1)
		legend2 = plt.legend(handles=[line2], loc=3)
		bx = plt.gca().add_artist(legend2)
		plt.legend(handles=[line3], loc=4)

		#plt.show()
		plt.draw()
		plt.pause(1) 
		input("<Hit Enter To Close>")
		plt.close(fig3)

	#histogram plot
	else: 

		fig4 = plt.figure("Drift 2")

		N = gen_max+1
		ind = np.arange(N)
		width = 0.5       

		AAAa_freq = [sum(x) for x in zip(AA_freq, Aa_freq)]
		# print(AAAa_freq)
		p1 = plt.bar(ind, AA_freq, width, color='red')
		p2 = plt.bar(ind, Aa_freq, width, bottom=AA_freq)
		p3 = plt.bar(ind, aa_freq, width, bottom=AAAa_freq)

		plt.title('Frequency of allele types over the course of the generations')
		plt.ylabel('frequency of allele types')
		plt.xlabel('generations')
		plt.axis([0, gen_max+1, 0, 100])
		plt.legend((p1[0], p2[0], p3[0]), ('AA', 'Aa', 'aa'))

		#plt.show()
		plt.draw()
		plt.pause(1) 
		input("<Hit Enter To Close>")
		plt.close(fig4)


geneticDrift1()
geneticDrift1(histogram = True)

geneticDrift2()
geneticDrift2(histogram = True)


# if __name__ == '__main__':
#     main()


