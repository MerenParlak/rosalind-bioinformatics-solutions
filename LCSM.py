with open("rosalind_lcsm.txt", "r") as file: 
    sequences = {}
    current_id = ""
        
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:] 
            sequences[current_id] = ""
        else:
            sequences[current_id] += line

shortest = min(sequences.values(), key=len)

for lenght in range(len(shortest),0,-1): #length
    for i in range(len(shortest) - lenght + 1): #starting index
        motif = shortest[i:i+lenght]
        if all(motif in seq for seq in sequences.values()):
            exit(print(motif))                

            