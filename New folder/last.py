import sys

input = sys.stdin.readline

n, w, h = map(int, input().split())

env = []
for i in range(n):
    wi, hi = map(int, input().split())
    if wi > w and hi > h:      
        env.append((wi, hi, i + 1))  

if not env:
    print(0)
    sys.exit(0)


env.sort(key=lambda x: (x[0], -x[1]))

m = len(env)


tail = []
prev = [-1] * m

for i in range(m):
    hi = env[i][1]

    
    lo, hi_idx = 0, len(tail)
    while lo < hi_idx:
        mid = (lo + hi_idx) // 2
        if env[tail[mid]][1] < hi:    
            lo = mid + 1
        else:
            hi_idx = mid
    pos = lo

    if pos > 0:
        prev[i] = tail[pos - 1]
    if pos == len(tail):
        tail.append(i)
    else:
        tail[pos] = i


length = len(tail)
last_idx = tail[-1]


ans = []
while last_idx != -1:
    ans.append(env[last_idx][2])  
    last_idx = prev[last_idx]

ans.reverse()

print(length)
print(*ans)
