def lis(arr):
    n = len(arr)
    tail = [arr[0]]
    for i in range(1,n):
        if(arr[i]>tail[-1]):
            tail.append(arr[i])
        else:
            c = ceilIdx(tail,arr[i])
            tail[c] = arr[i]
    return len(tail)

def ceilIdx(tail,x):

    l = 0
    r = len(tail)-1
    while r>l:
        m = l+(r-l)//2
        if(tail[m]>x):
            r = m
        else:
            l = m+1

    return r

arr = [3,10,20,4,6,7]
print(lis(arr))