def calculate_probability(k, m, n):
    total=k + m + n
    #situation 1: both alleles are rescessive
    n_n = (n / total) * ((n - 1) / (total - 1)) * 1
    #situation 2: both alleles are dominant
    m_m = (m / total) * ((m - 1) / (total - 1)) * 0.25
    #situation 3: one allele is dominant and the other is recessive
    m_n = (m / total) * (n / (total - 1)) * 0.5
    #situation 4: one allele is dominant and the other is recessive
    n_m = (n / total) * (m / (total - 1)) * 0.5

    not_probability_sum= n_n + m_m + m_n + n_m
    probability_sum = 1 - not_probability_sum
    
    return round(probability_sum, 5)

k, m, n = map(int, open(r"C:\Users\LEGION\Desktop\Bioinformatik\rosalind_iprb.txt", "r").read().strip().split())
print(calculate_probability(k,m,n))