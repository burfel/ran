def extract_cds(gff_lines, seq):
	print ("SEQ:", seq)

	for line in gff_lines:
		print (line)

with open("CAUH01000968.gff") as gff_file:
	gff_lines = gff_file.readlines()
	seq = gff_lines.pop()

extract_cds(gff_lines, seq)

