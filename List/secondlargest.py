# Finding the second largest element in the list

# l = [10,40,50,60]  since the second largest element is 50

def seclargest(l):

    if len(l)<=1:
        return None
    
    lar = l[0]
    slar = None

    for i in l[1:]:
        if i > lar:
            slar = lar
            lar = i
        elif i!=lar:
            if slar == None or slar < i:
                slar = i

    return slar

l = [10,40,50,60]
print(seclargest(l))
