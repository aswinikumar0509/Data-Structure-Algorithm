# fing the gcd of the two number 

def gcd(a,b):

    while a!=b:

        if a > b:
            a = a-b
        else:
            b = b-a

    return a

if __name__ == '__main__':
    a = 12
    b = 15
    print(gcd(a,b))
