def maxactivity(arr):

    n = len(arr)

    arr.sort(key=lambda x : x[1])
    prev = 0
    res = 1
    for  curr in range(1,n):
        if arr[curr][0] >= arr[prev][1]:
            res+=1
            prev = curr
    return res

arr = [(12,25),(10,20),(20,30)]
print(maxactivity(arr))

 
