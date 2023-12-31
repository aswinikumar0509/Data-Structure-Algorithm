# Reversing the list 

def reverse(l):

    s = 0 
    e = len(l)-1

    while s < e:
        l[s],l[e] = l[e],l[s]
        s+=1
        e-=1
    return l

l = [10,20,40,50]
print(reverse(l))