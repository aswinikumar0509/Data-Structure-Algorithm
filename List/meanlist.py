# find the mean of the list

def mean(l):

    sum = 0
    for x in l:
        sum = sum+x

    n=len(l)
    return sum/n

l = [34,87,65,43]

print(mean(l))
