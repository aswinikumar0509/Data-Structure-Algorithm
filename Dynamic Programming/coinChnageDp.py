def countways(coin,s):
    n = len(coin)
    dp = [[0 for x in range(s+1)]
          for x in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(1,s+1):
                dp[i][j] = dp[i-1][j]
                if j>=coin[i-1]:
                    dp[i][j]+=dp[i][j-coin[i-1]]

    return dp[n][s]

coin = [1,2,3]
s = 4
print(countways(coin,s))