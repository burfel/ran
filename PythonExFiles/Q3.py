import matplotlib.pyplot as plt

# A function to produce the plots
def plotCU(codon_usage, gene_codon_usage):

	# Initialise lists for the plot data
	x_data = range(len(codon_usage))
	y_data = codon_usage
	y_data2 = gene_codon_usage
	
	# Create and display the plots
	plt.subplot(2, 1, 1)
	plt.bar(x_data, y_data)
	plt.xlabel("Codon")
	plt.ylabel("Genome Codon Usage")
	plt.title("Codon Usage")

	plt.subplot(2, 1, 2)
	plt.bar(x_data, y_data2)
	plt.xlabel("Codon")
	plt.ylabel("Gene Codon Usage")
	plt.show()


# Declare list for the codon usage data
codon_usage = []

# Read the codon usage file and store the data
with open ('CodonUsage.txt') as infile:
	for line in infile:
		l = line.split()
		codon_usage.append(float(l[2]))

# Declare list for the gene codon usage data
gene_codon_usage = []

# Initially fill the gene codon usage data list with 0's
for i in range(len(codon_usage)):
	gene_codon_usage.append(0)


# Call the plotting function
plotCU(codon_usage, gene_codon_usage)


