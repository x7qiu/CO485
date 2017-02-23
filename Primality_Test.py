import random
import GCD
import Jacobi

def Trial(n):
    if i < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True 

def Fermat_Test(n, k):
    for i in range(k):
        a = random.randint(1,n-1)
        t = pow(a, n-1, n)
        if t != 1:
            print "Composite"
            return False
    print "Probably prime"
    return 

def SS_Test(n, k):
    for i in range(k):
        a = random.randint(1, n-1)
        d = GCD.GCD(a, n)
        if d > 1:
            print "Composite"
            return False
        t1 = pow(a, (n-1)/2, n)
        t2 = Jacobi.Jacobi(a, n)
        t2 = t2%n                   
        #print "t1 is", t1, "t2 is", t2
        if t1 != t2:
            print "Composite"
            return False
    print "Probably Prime"
    return 

def rewrite(n):
    """ rewrite the number n into (2**r)*d where d is odd"""
    r = 0
    while n%2 == 0: 
        n = n/2
        r = r+1
        if n == 0:
            break
    return r, n
        
def Miller_Rabin(n, k):
    r, d = rewrite(n-1)
    for i in range(k):
        a = random.randint(1,n-1)
        x = pow(a, d, n)
        if x == 1:
            continue
        else:
            count = 0   # count the number of modular equal to -1 mod n
            for j in range(r):
                if pow(a, (2**j)*d,n) == -1%n:
                    count = count + 1
            if count == 0:
                print "Composite"
                return False
            else:
                continue
    print "Probably Prime"
    return 

