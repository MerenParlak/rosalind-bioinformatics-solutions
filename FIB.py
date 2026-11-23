def rabbits(n,k):
    rabbits = [0] * (n + 1) #We create a list of size n+1 to store the number of rabbit pairs for each month, initialized to 0
    rabbits[1] = 1  
    rabbits[2] = 1
    for i in range(3, n + 1):
        rabbits[i] = rabbits[i - 1] + k * rabbits[i - 2]

    return rabbits[n]   #This for loop calculates the number of rabbit pairs for each month from 3 to n using the recurrence relation, and finally returns the number of rabbit pairs in month n.

#strip() removes any leading/trailing whitespace, and split() separates the two integers
n, k = map(int, open("rosalind_fib.txt").read().strip().split())   
print(rabbits(n, k))