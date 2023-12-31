# Checking the number is palindrome or not

def ispal(number):

    temp = number   
    rev = 0

    while temp!=0:
        ld = temp%10
        rev = rev*10+ld
        temp = temp//10

    if rev == number:
        return ("yes")
    else:
        return ("No")
    
number = 4554
print(ispal(number))
        