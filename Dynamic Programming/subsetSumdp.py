def countSubset(arr,sum):
    n = len(arr)

    mat = [[0 for i in range(sum+1)]
           for i in range(n+1)]
    
    for i in range(n+1):
        mat[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j<arr[i-1]:
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j] + mat[i-1][j-arr[i-1]]

    return mat[n][sum]


arr = [2,5,3]
sum = 5
print(countSubset(arr,sum))