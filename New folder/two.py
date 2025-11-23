d, sumTime = map(int, input().split())

mins = []
maxs = []
for _ in range(d):
    mn, mx = map(int, input().split())
    mins.append(mn)
    maxs.append(mx)

sumMin = sum(mins)
sumMax = sum(maxs)


if sumTime < sumMin or sumTime > sumMax:
    print("NO")
else:
    print("YES")
    schedule = mins[:]  
    remaining = sumTime - sumMin

    for i in range(d):
        
        can_add = maxs[i] - mins[i]
        add = min(remaining, can_add)
        schedule[i] += add
        remaining -= add
        if remaining == 0:
            break

    print(*schedule)
