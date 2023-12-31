# Find the even and the odd number in the list

def evenodd(l):

    even = []
    odd = []

    for x in l:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    return even,odd

l = [10,35,40,25]
print(evenodd(l))