with open ("rosalind_iev.txt", "r") as file:
    data = list(map(int, file.read().strip().split()))
probs = [1, 1, 1, 0.75, 0.5, 0]
final = [d * p* 2 for d, p in zip(data, probs)]  #Can make a for loop and add in a empty list 
print(sum(final))