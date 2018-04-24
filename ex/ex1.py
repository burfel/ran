''' COMPUTING: Assessed Exercise No. 1
	Felicia Burtscher
'''

''''

	DESCRIPTION: 
		The following python script reads the file seq_sample.fastq and filters out any
		read pairs where at least one of the sequences has an average qscore below 30 
		(see task Exercise No. 1).

	INPUTS: 
		The script takes the given fastq file containing the samples as described in the task 
		(each set of paired end sequences covering 8 lines).

	OUTPUTS: 
		2 files:
		- goodquality_seqs.fasta contains the sequences where both reads have an average score of at least 30
		- badquality_seqs.fasta contains the rest of the sequences, ie the sequences that have at least 1 read with an average score below 30

	NOTE:
		The fastq file has to be located in the same directory as the script is run.
		The commented print functions in the following script can be ignored and are solely for debugging purposes.

'''

#!/usr/bin/env python3
import os

# function that calculates the average qscore of a string
def averageQscore(sequence):
	total_qscore = 0
	for qs in range(0, len(sequence)): 
		val = ord(sequence[qs])-64 # calculating actual score from the ascii values of the characters
		# print(val)
		total_qscore += val # adding the scores up
	average_qscore = total_qscore / len(sequence) # calculating average qscore
	# print(average_qscore)
	return average_qscore

# the output files:
# file that will contain the sequences where both reads have an average score of at least 30
out_file1 = open("goodquality_seqs.fastq", "w") 
# file that will contain the rest of the sequences, ie those sequences that have at least 1 read with an average score below 30
out_file2 = open("badquality_seqs.fastq", "w") 

goodquality_seqs = []
badquality_seqs = []


# the following code filters the sequences depending on the average phred qscores of their two reads as required

with open("seq_sample.fastq") as fastq_file:
	# reading file to a list
	fastq_list = fastq_file.read().splitlines()
	# print(fastq_list)
	# print("\n", "number of lines: ", len(fastq_list), "\n")
	# loops over set of paired end sequences 
	for qs in range(0,len(fastq_list),8): 
 		# print(fastq_list[qs+3])
 		# print(averageQscore(fastq_list[qs+3]))
 		# print(qs+3)
 		# print(fastq_list[qs+7])
 		# print(averageQscore(fastq_list[qs+7]))
 		# print(qs+7)
 		# print((averageQscore(fastq_list[qs+3]) >= 30) and (averageQscore(fastq_list[qs+7]) >= 30)) 
		if (averageQscore(fastq_list[qs+3]) >= 30) and (averageQscore(fastq_list[qs+7]) >= 30): # if both reads have an average score of at least 30
				# print(qs, ": good quality")
				goodquality_seqs.append(qs) # then it goes in the goodquality sequence file
				for qqs in range(8):
 					out_file1.write(fastq_list[qqs+qs]+'\n')
		else: 
			# print(qs, ": bad quality")
			badquality_seqs.append(qs) # otherwise it goes in the badquality file
			for qqs in range(8):
 				out_file2.write(fastq_list[qqs+qs]+'\n')

# print("good quality sequences: ", goodquality_seqs)
# print("# good quality sequences:", len(goodquality_seqs))
# print("bad quality sequences: ", badquality_seqs)
# print("# bad quality sequences:", len(badquality_seqs))
