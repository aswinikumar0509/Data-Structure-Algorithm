M=1000
N=1000

memo = [[-1]*N for i in range(M)]

def lcs(s1,s2,n,m):
    if memo[n][m]!=-1:
        return memo[n][m]
        
    if m==0 or n==0:
        memo[n][m] = 0
    else:
        if(s1[n-1]==s2[m-1]):
            memo[n][m] = 1 + lcs(s1,s2,n-1,m-1)
        else:
            memo[n][m] = max(lcs(s1,s2,n,m-1),lcs(s1,s2,n-1,m))
            
    
    return memo[n][m]
    


s1='AXYZ'
s2='BAZ'

print(lcs(s1,s2,len(s1),len(s2)))
