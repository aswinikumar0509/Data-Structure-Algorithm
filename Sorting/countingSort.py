def countingsort(arr,k) :
    output = [0] * len(arr)
    count = [0] * k
    for x in arr :
        count[x] += 1
    
    for i in range(1,k) :
        count[i] += count[i - 1]
    for x in reversed(arr) :
        output[count[x] - 1] = x
        count[x] -= 1 
    for i in range(len(arr)) :
        arr[i] = output[i]
    
    print(arr)
    
arr = [1,4,4,1,0,1]
countingsort(arr,5)
