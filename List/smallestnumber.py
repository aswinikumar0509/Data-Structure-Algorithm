#finding the smallest number in the list with given k

def small(l,k):

    res = []

    for x in l:
        if x < k:
            res.append(x)

    return res

l = [10,47,90,45]
k = 50
print(small(l,k))            