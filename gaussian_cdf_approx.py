import math

def phi(z):
    return math.exp(-z * z / 2.0) / math.sqrt(2.0 * math.pi)

def Phi(z, terms=5):
    sum_series = 0
    for n in range(terms):
        numerator = z ** (2 * n + 1)
        denominator = 1
        for i in range(1, 2 * n + 2, 2):
            denominator *= i  
        sum_series += numerator / denominator
    return 0.5 + phi(z) * sum_series
      
z = 1.0
print(f"Phi({z}) ≈ {Phi(z)}")    
