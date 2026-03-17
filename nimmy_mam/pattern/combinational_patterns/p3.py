#combinational pattern
n=int(input("enter the number : "))
noc=1
for i in range(1,n*2):
    for j in range(1,noc+1):
        print("* ",end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
print("===========================")

n=int(input("enter the number : "))
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("*",end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
print("===========================")

n=int(input("enter the number : "))
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("* ",end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
print("===========================")

n=int(input("enter the number : "))
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc*2):
        print("*",end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
print("========================")

n=int(input("enter the number : "))
noc=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        print("* ",end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1
print("========================")


n=int(input("enter the number : "))
noc=n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("*",end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1
print("========================")


n=int(input("enter the number : "))
noc=n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print("* ",end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1
print("========================")


n=int(input("enter the number : "))
noc=n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc*2):
        print("*",end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1
