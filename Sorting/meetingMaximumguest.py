## Metting the maximin gueest in the party

def meetMax(arr,dep):
    arr.sort()
    dep.sort()
    n = len(arr)
    i,j = 1,0
    curr , res = 1,1
    while (i<n  and j<n):
        if(arr[i]<=dep[j]):
            curr+=1
            i+=1
        else:
            curr-=1
            j+=1
        res = max(res,curr)

    return res

arr = [900,600,700]
dep = [1000,800,730]

print(meetMax(arr,dep))