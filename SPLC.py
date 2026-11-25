codon_dictionary = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}

with open("rosalind_splc.txt", "r") as file: 
        sequences = {}
        current_id = ""
        
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_id = line[1:] 
                sequences[current_id] = ""
            else:
                sequences[current_id] += line

seq_list = list(sequences.values())
dna = seq_list[0]
introns = seq_list[1:]

for intron in introns:
    dna = dna.replace(intron,"")
rna = dna.replace("T","U")

def rna_to_protein(rna_sequence):
    protein_sequence = ""
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        if codon in codon_dictionary:
            amino_acid = codon_dictionary[codon]
            if amino_acid == "Stop":
                break
            protein_sequence += amino_acid
    return protein_sequence
print(rna_to_protein(rna))