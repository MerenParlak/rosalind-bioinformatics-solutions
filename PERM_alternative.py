import math

n=3

perms=[[1]]
for num in range(2, n+1):
    new_perms = []
    for p in perms:
        for i in range(len(p) + 1):
            new_perms.append(p[:i] + [num] + p[i:])
    perms = new_perms
print(math.factorial(n))
for p in perms:
    print(*p)