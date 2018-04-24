def build_pwm(dna_mat)

	n = len(dna_mat[0])
	A = [0] * n
	C = [0] * n
	G = [0] * n
	T = [0] * n
	pwm = [A, C, G, T]
	for dna in dna_mat:
		for i in range (1, n): 
			base = dna[i]
			if base = 'A':
				pwm[0][index] +=1
			else if base = 'C':
				pwm[1][index] +=1
			else if base = 'G':
				pwm[2][index] +=1
			else:
				pwm[3][index] +=1

		return pwm

with open('seq.msa') as infile:
	for line in infile.readlines():
		arr = line.split()
		dna_mat.append(arr[0])		

pwm = build_pwm(dna_mat)
print (pwm)
