dna_seq= open("rosalind_revc.txt").read().strip()
complement_seq = dna_seq[::-1].translate(
    str.maketrans("ATCG", "TAGC"))
print(complement_seq)