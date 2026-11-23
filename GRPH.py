with open("rosalind_grph.txt", "r") as file: 
    sequences = {}
    current_id = ""
        
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:] 
            sequences[current_id] = ""
        else:
            sequences[current_id] += line
#print(sequences.items())

for id1, seq1 in sequences.items():
    for id2, seq2 in sequences.items():
        if seq1 != seq2 and seq1[-3:] == seq2[:3]:
            print(f"{id1} {id2}")