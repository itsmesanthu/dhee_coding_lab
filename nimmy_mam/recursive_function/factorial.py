def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
n=int(input("enter the num:"))
s=fact(n)
print(f" the factorial of this number {n} is {s}")