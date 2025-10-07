def printnum(n):
    if n == 1:   # base case
        return 1
    fact = n + printnum(n-1)   # use recursive call
    return fact    

x = printnum(5)
print(x)
