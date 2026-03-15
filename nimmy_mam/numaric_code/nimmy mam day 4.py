''''#incremnet for looping
n=int(input("enter the number : "))
m=int(input("enter the difference to increment :"))
for i in range(2, (n+1), +m):
    print(i,end=" ")
print("\n last updated :",i)
#decrement  for looping
n=int(input("enter the number : "))
m=int(input("enter the difference to decrement :"))
for i in range(n, (1-1), -m):
    print(i,end=" ")
print("\n last updated :"
#-WAL to print 1 to 8(n) with a incrementing difference starting form the 1
n=int(input("enter the number"))
i=1
d=1
while i<=n:
    print(i,end=' ')
    i=i+d
    d=d+1
print("\nlast updated i : ",i)
#WAL to print nurtural number up to ‘n’ included in an incrementing order
n=int(input("enter the number: "))
i=2
while i<=n:
    print(i,end=' ')
    i=i+1
print("\nlast updated i : ",i)
#WAL to print nurtural number up to starting form  ‘n’ included in an decrementing order with difference of 2
n=int(input("enter the number: "))
while n>0:
    print(n,end=' ')
    n=n-2
print("\nlast updated n : ",n)
while True:
    n=int(input("enter the number: "))
    if n==0:
        break
        print("thank you for executing ")
    elif n==3 or n ==5:
        continue
    else:
        print(f"the enter number is {n}")'''