import random

def Trial(n):
    list = []
    for i in range(2, abs(n)):
        if n%i == 0:
            list.append(i)
            list.extend(Trial(n/i))
            return list
    list.append(n)
    return list

"""
# the following code does not work, giving [2,2,2,2,2] on Generate_Primes(5).
def Generate_Primes(t):
    primes = []
    for i in range(t):
        primes.append(next(gen_primes()))
    return primes
"""

def Generate_Primes(t):
    gen = gen_primes()
    primes = []
    for i in range(t):
        primes.append(next(gen))
    return primes

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1

   
def Random_Squares(n, t):
    base =  Generate_Primes(t)
    prime_t = max(base)
    relations = []
    count = 0
    seen = set()
    
    while True:
        a = random.randint(2,n-1)
        b = pow(a, 2, n)
        if b not in seen:
            seen.add(b)
        factors = Trial(b)
        if max(factors) <= prime_t:
            relations.append((b, factors))
            count = count + 1
            if count >= t+10:
                break
    print relations
             
def find_even_subset(list_of_list):
    
