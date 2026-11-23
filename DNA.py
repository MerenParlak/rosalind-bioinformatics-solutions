from collections import Counter     

def count_nucleotides(dna_sequence):
    nucleotide_counts = Counter(dna_sequence)

    return f"{nucleotide_counts['A']} {nucleotide_counts['C']} {nucleotide_counts['G']} {nucleotide_counts['T']}"

with open('rosalind_dna.txt', 'r') as file:
    sample_dna = file.read().strip()

print(count_nucleotides(sample_dna))
