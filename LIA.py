import math
with open ("rosalind_lia.txt", "r") as file:
    k, N = list(map(int, file.read().strip().split()))
P = 2**k
probability = sum(math.comb(P, i) * (0.25 ** i) * (0.75 ** (P - i)) for i in range(N, P + 1))

print(round(probability, 3))