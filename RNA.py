dna_seq= open("rosalind_rna.txt").read().strip() 
rna_seq = dna_seq.replace("T", "U")
print(rna_seq)