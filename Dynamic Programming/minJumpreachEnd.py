import sys

def minJumps(arr,n):

    if n==1:
        return 0
    res = sys.maxsize

    for i in range(n-1):
        if i+arr[i]>=n-1:
            sub_res = minJumps(arr,i+1)

            if sub_res!=sys.maxsize:
                res = min(res,sub_res+1)

    return res

arr = [3,4,2,1,2,1]
n = len(arr)

print(minJumps(arr,n))