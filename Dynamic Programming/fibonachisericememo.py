memo = [None]*100

def fib(n):
    if memo[n]!=None:
        return memo[n]
    if n==0 or n==1:
        memo[n] = n

    else:
        memo[n] = fib(n-1) + fib(n-2)

    return memo[n]

n=5
print(fib(6))