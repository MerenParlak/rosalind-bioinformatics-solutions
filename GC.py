def finding_highest_gc_content(file_path):
    # Read the FASTA file and store sequences in a dictionary
    with open(file_path, "r") as file: 
        sequences = {}
        current_id = ""
        
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_id = line[1:] 
                sequences[current_id] = ""
            else:
                sequences[current_id] += line
    
    # Calculate GC content for each sequence and find the one with the highest GC content    
    highest_gc_content = 0.0
    highest_gc_id = ""
        
    for seq_id, seq in sequences.items():
        gc_count = seq.count("G") + seq.count("C")
        gc_content = (gc_count / len(seq)) * 100
            
        if gc_content > highest_gc_content:
            highest_gc_content = gc_content
            highest_gc_id = seq_id
        
    return f"{highest_gc_id}\n{highest_gc_content:.6f}" 

result = finding_highest_gc_content(r"C:\Users\LEGION\Desktop\Bioinformatik\rosalind_gc.txt")
print(result)