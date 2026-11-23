def rabbits (n,m):
    ages = [1] + [0] * (m-1)
    for i in range(0,n-1):
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)
print(rabbits(100,17))