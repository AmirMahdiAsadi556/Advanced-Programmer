import math

def phi(x):
    return math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi)

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x - mu) / sigma) / sigma 
   
print(pdf(1, mu=0, sigma=1))
print(pdf(1, mu=1, sigma=2))
