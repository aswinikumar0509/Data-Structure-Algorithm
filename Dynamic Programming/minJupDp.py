import sys

def minJump(arr):
    n = len(arr)
    dp = [sys.maxsize]*n
    dp[0] = 0

    for i in range(1,n):
        for j in range(i):
            if(i<=j+arr[j]) and (dp[j]!=sys.maxsize):
                dp[i] = min(dp[i],dp[j]+1)
                break
    return dp[n-1]


arr =  [3,4,2,1,2,1]
n = len(arr)

print(minJump(arr))