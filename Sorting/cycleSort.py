def cyclesortdist(arr) :
    w = 0
    for cs in range(len(arr) - 1) :
        item = arr[cs]
        pos = cs
        for i in range(cs+1, len(arr)) :
            if arr[i] < item :
                pos = pos + 1 
        if pos == cs :
            continue
        
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        w += 1
        
        while pos != cs :
            pos = cs 
            for i in range(cs+1, len(arr)) :
                if arr[i] < item :
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            w += 1
    
    
    
arr = [20,40,30,10,50]
n = len(arr)
cyclesortdist(arr)

for i in range(0, n) :
    print(arr[i])
