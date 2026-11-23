dna_sequences = open("rosalind_hamm.txt", "r").read().strip().splitlines() #['GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT']

mutation_count = 0

for letter_1, letter_2 in zip(dna_sequences[0], dna_sequences[1]):
    if letter_1 != letter_2:
        mutation_count += 1

print(mutation_count)

#for i in range(len(dna_sequences[0])):    
#    if dna_sequences[0][i] != dna_sequences[1][i]:
#        mutation_count += 1