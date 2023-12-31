# Finding the largest element in the list 

def largest(l):

    if not l:
        return None
    else:

        res = l[0]

        for i in range(1,len(l)):
            if l[i] > res:
                res = l[i]
        
        return res
    
l = [10,40,30,70]
print(largest(l))