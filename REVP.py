with open("rosalind_revp.txt", "r") as file: 
        sequences = {}
        current_id = ""
        
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_id = line[1:] 
                sequences[current_id] = ""
            else:
                sequences[current_id] += line

dna_sequence = list(sequences.values())[0]  
def reverse_complement(seq):
    return seq.translate(str.maketrans("ATCG", "TAGC"))[::-1]

for i in range(len(dna_sequence)):
     for length in range(4, 13 , 2):
          if i + length <= len(dna_sequence):
            piece = dna_sequence[i: i+length]
            if piece == reverse_complement(piece):
                print(i + 1 ,length)
