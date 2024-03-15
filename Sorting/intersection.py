#intersection of the two array

def intersection(arr1,arr2,m,n):
    i,j = 0,0

    while i<m and j<n:
        if arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        else:
            print(arr2[j],end = "")
            i+=1
            j+=1
            