dna_codons = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "Stop", "TAG": "Stop",
    "TGT": "C", "TGC": "C", "TGA": "Stop", "TGG": "W",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

with open("rosalind_orf.txt", "r") as file: 
        sequences = {}
        current_id = ""
        
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_id = line[1:] 
                sequences[current_id] = ""
            else:
                sequences[current_id] += line

dna = str(list(sequences.values())[0])
comp_dna = dna.translate(str.maketrans("ATCG", "TAGC"))[::-1]
sequences = [dna, comp_dna]
proteins = set()
for seq in sequences:
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            protein = ""
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                aa = dna_codons[codon]
                if aa == "Stop":
                    proteins.add(protein)
                    break
                protein += aa

for p in proteins:
    print(p)