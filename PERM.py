from itertools import permutations

n = 6
perms_list = list(permutations(range(1, n + 1)))

with open("output.txt", "w") as out:
    out.write(f"{len(perms_list)}\n")
    for p in perms_list:
        out.write(" ".join(map(str, p)) + "\n")
