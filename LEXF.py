from itertools import product
with open ("rosalind_lexf.txt","r") as file:
    lines = file.read().splitlines()

alphabet = lines[0].split()
n = int(lines[1])

k_mer = product(alphabet, repeat=n)

with open("output.txt", "w") as out:
    for p in k_mer:
        out.write("".join(p)+ "\n") 