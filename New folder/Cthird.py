import sys
input = sys.stdin.readline

BIG = 10**9

t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    
    inType1 = [False] * n
    inType2 = [False] * n
    type1_intervals = []
    type2_intervals = []
    
    queries = []
    for _q in range(q):
        c, l, r = map(int, input().split())
        l -= 1  
        r -= 1
        queries.append((c, l, r))
        if c == 1:
            for i in range(l, r + 1):
                inType1[i] = True
        else:
            for i in range(l, r + 1):
                inType2[i] = True
    
    a = [BIG] * n
    

    for c, l, r in queries:
        if c == 1:
            placed = False
            for i in range(l, r + 1):
                if not inType2[i]:
                    a[i] = k
                    placed = True
                    break
            
    
  
    B_indices = [i for i in range(n) if not inType1[i]]
    
 
    if k > 0:
        for idx, pos in enumerate(B_indices):
            a[pos] = idx % k
    
    print(*a)
