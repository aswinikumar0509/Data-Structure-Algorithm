# create the union of the array

def union(a,b,n,m):

    result = [0 for i in range(n+m)]

    index , left,right = 0,0,0

    while left<n and right < m:
        if(a[left]<b[right]):
            if(index!=0 and a[left]==result[index-1]):
                left+=1
            else:
                result[index]=a[left]
                left+=1
                index+=1
        else:
            if (index!=0 and b[right]==result[index-1]):
                right+=1
            else:
                result[index]=b[right]
                right+=1
                index+=1


    while (left<n):
        if(index!=0 and a[left]==result[index-1]):
            left+=1

        else:
            result[index]=a[left]
            left+=1
            index+=1

    while (right<m):
        if (index!=0 and b[right]==result[index-1]):
            right+=1
        else:
            result[index]=b[right]
            right+=1
            index+=1
    print("Union:", *result[:index])


a = [10, 15]
b = [5, 6, 6, 30, 40]
n = len(a)
m = len(b)

print(union(a,b,n,m))