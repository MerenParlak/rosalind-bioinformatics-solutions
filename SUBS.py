with open("rosalind_subs.txt", "r") as file:
    dna_seq, motif = file.read().strip().splitlines()

positions = []
for i in range(len(dna_seq) - len(motif) + 1):
    if dna_seq[i:i+len(motif)] == motif:
        positions.append(i+1)

print(*positions) 