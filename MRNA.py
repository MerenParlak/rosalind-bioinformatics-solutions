codon_counts = {
    'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4,
    'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2,
    'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4
}

def protein_to_mrna(protein_sequence):
    mrna_sequence = 3
    for amino_acid in protein_sequence:
        if amino_acid in codon_counts:
            mrna_sequence = (mrna_sequence * codon_counts[amino_acid]) % 1000000
    return mrna_sequence

with open("rosalind_mrna.txt", "r") as file:
    protein = file.read().strip() 

print(protein_to_mrna(protein))