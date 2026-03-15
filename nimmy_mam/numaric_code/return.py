'''def printnum4(n):
    print(n)
    printnum3(n-1)
    return
def printnum3(n):
    print(n)
    printnum2(n-1)
    return
def printnum2(n):
    print(n)
    printnum1(n-1)
    return
def printnum1(n):
    print(n)
    printnum(n-1)
    return
def printnum(n):
    print(n)
    return
n=7
printnum4(n)'''
'''def printnum(n):
        if n<=0:
            return
        printnum(n-1)
        print(n , end="")
n=int(input("enter the number :"))
printnum(n)'''


def printnum(n):
    if n <= 0:
        return

    printnum(n - 1)  # increasing part
    print(n, end="")
    print(n, end="")
    printnum(n - 1)  # decreasing part


n = int(input("Enter the number: "))
printnum(n)