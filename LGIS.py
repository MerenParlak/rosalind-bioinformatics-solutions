with open("rosalind_lgis.txt", "r") as file:
    lines = file.read().splitlines()

pi = list(map(int, lines[1].split()))
def longest_sequence(seq):
    m = len(seq)
    dp = [1] * m
    prev = [-1] * m

    for i in range(m):
        for j in range(i):
            if seq[j] < seq[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    ind = dp.index(max(dp))
    lis = []
    while ind != -1:
        lis.append(seq[ind])
        ind = prev[ind] 
    lis.reverse()
    return lis
lis = longest_sequence(pi)
lds = longest_sequence(pi[::-1])[::-1]

with open("output.txt", "w") as out:
    out.write(" ".join(map(str, lis)) + "\n")
    out.write(" ".join(map(str, lds)) + "\n")