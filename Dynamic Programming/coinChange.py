#Coin Change count Combination

# def countWays(coin,n,s):
#     # if s==0:
#     #     return 1
#     # if s<0:
#     #     return 0
#     # if n==0:
#     #     return 0
    
#     # return countWays(coin,n,s-coin[n-1])+countWays(coin,n-1,s)

#     if s == 0:
#         return 1
#     if s<0:
#         return 0
#     if n == 0:
#         return 0
    
#     return countWays(coin,n,s-coin[n-1])+ countWays(coin,n-1,s)

# coin = [2,5,3]
# n = 2
# s = 5
# print(countWays(coin,n,s))

def countWays(coins,n,s):
    if s == 0:
        return 1
    if s<0:
        return 0
    if n == 0:
        return 0
    
    return countWays(coins,n,s-coins[n-1])+ countWays(coins,n-1,s)
    
    
arr = [2,5,3]
n = 3
s = 5

print(countWays(arr,n,s))