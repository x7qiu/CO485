import Factorization
import Primality_Test
from collections import Counter

def Legendre(a, p):
    # assume p is prime, odd
    a = a%p
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a == -1:
        return pow(-1, (p-1)/2)
    if a == 2:
        return pow(-1, (p**2 - 1)/8)
    else:
        factors = Factorization.Trial(a)
        if factors[0] == a:     # if a is prime
            return Legendre(p, a) * pow(-1, (a-1)*(p-1)/4)
        else:
            ans = 1
            for i in factors:
                ans = ans * Legendre(i,p)
            return ans

def Jacobi(a, n):
    # assume n>=3, odd
    factors = Factorization.Trial(n)
    factors = Counter(factors)

    ans = 1
    for i in factors:
       ans = ans * Legendre(a, i)
    return ans


