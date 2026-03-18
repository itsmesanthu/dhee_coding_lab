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

#reverse combination pattern
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

#diamond pattern
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

#special diamond pattern
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

#K pattern
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

#reverse K pattern
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

#hourglass patern
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

#special hourglass pattern
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
