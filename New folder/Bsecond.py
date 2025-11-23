import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    s = input().strip()

    c4 = s.count('4')
    c8 = s.count('8')

    ax = abs(x)
    ay = abs(y)

    
    if ax + ay <= c4 + 2 * c8 and max(ax, ay) <= c4 + c8:
        print("YES")
    else:
        print("NO")
