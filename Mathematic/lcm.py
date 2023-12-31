# finding the lcm of two number

def gcd(a,b):

    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b // gcd(a,b)

if __name__ == '__main__':
    a = 12
    b = 15

    print(lcm(a,b))