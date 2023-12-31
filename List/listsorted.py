# Checking the list is shorted or not

def sorted(l):

    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i = i+1

    return True

l = [14,98,21]
if l == True:
    print("Yes")
else:
    print("No")