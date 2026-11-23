with open("rosalind_cons.txt", "r") as file: 
    sequences = {}
    current_id = ""
        
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:] 
            sequences[current_id] = ""
        else:
            sequences[current_id] += line
dna_string = list(sequences.values())
#print(dna_string)
n=len(dna_string[0])

profile = {
    "A": [0] * n, 
    "C": [0] * n,
    "G": [0] * n,
    "T": [0] * n
}   

for seq in dna_string:
    for i in range(n):
        Nukletoid = seq[i]
        profile[Nukletoid][i] += 1

#print(profile)

concensus = ""
for i in range(n):
    max_count = -1
    max_nucleotide = ""
    for nucleotide in "ACGT":
        if profile[nucleotide][i] > max_count:
            max_count = profile[nucleotide][i]
            max_nucleotide = nucleotide

    concensus += max_nucleotide
print(concensus)
for nuc in "ACGT":
    sayilar_str = " ".join(map(str, profile[nuc]))
    print(f"{nuc}: {sayilar_str}")