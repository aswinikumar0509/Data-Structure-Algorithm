# Count the digit in the given number

def countdigit(number):
    res = 0

    while number > 0:
        number = number//10
        res = res+1

    return res

number = 9865
print(countdigit(number))