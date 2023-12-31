# Checking the prime factor in the given number

def isprime(x):

    for i in range(2,x):
        if x%i==0:
            return False
    return True

def isprimefactor(n):

    for i in range(2,n+1):

        if isprime(i):

            x = i
            while n%x==0:
                print(i)
                x = x*i

n = 100
print(isprimefactor(n))