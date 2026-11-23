import urllib.request

with open("rosalind_mprt (1).txt", "r") as file:
    uniprot_ids = file.read().strip().splitlines()

for uniprot_id in uniprot_ids:
    accession = uniprot_id.split("_")[0]
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"

    with urllib.request.urlopen(url) as response:
        fasta_text = response.read().decode("utf-8")

    lines = fasta_text.strip().splitlines()
    seq = "".join(lines[1:]) #skipping the first line
    positions = []
    for i in range(len(seq) - 3):
        if seq[i] == "N" and seq[i+1] != "P" and seq[i+2] in "ST" and seq[i+3] != "P":
            positions.append(i + 1)
    if positions:
        print(uniprot_id)
        print(*positions)
