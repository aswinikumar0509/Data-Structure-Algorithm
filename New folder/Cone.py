import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    
    cnt = [0] * (n + 1)
    for x in arr:
        if x <= n:
            cnt[x] += 1  
    
    deletions = 0
    

    deletions += cnt[0]
    
    
    for x in range(1, n + 1):
        c = cnt[x]
        if c == 0:
            continue
        if c < x:
            deletions += c       
        else:
            deletions += c - x   
    
    print(deletions)
