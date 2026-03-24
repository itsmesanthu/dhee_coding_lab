'''n=int(input("enter the number: "))
noc=1
for i in range(1,n*2):
    for  j in range(1,noc+1):
        if j==1 or j==noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
print("=================================")

n=int(input("enter the number:"))
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for  j in range(1,noc+1):
        if j==1 or j==noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
print("=================================")

n=int(input("enter the number:"))
noc=1
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for  j in range(1,noc+1):
        if j==1 or j==noc:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc+=1
    else:
        noc-=1
print("===============================")

n=int(input("entrr the number : "))
noc=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        if j==1 or j==noc or  i==((n*2)-1 ) or i==1:
            print("*",end="")

        else:
            print(" ",end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1
print("===============================")

n=int(input("entrr the number : "))
noc=n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        if j==1 or j==noc or  i==((n*2)-1 ) or i==1:
            print("*",end="")

        else:
            print(" ",end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1
print("============================")

n=int(input("enter the number:"))
noc, nor=1,((n*2)-1)
for i in range(1,(n*2)):
    for j in range(1,(n*2)):
        if j==noc or j==nor or j==1 or j==((n*2)-1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc+=1
        nor-=1
    else:
        nor+=1
        noc-=1
print("=================================")

print("Number Patterns ")


n=int(input("enter thenumber :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()   
print("=================================")

n=int(input("enter the number :"))
for i in range(n,(1-1),-1):
    for j in range(n,(1-1),-1):
            print(i ,end="")
    print()
print("=================================")

n=int(input("enter the number :"))
for i in range(1,n+1):
    for j in range(1,n+1):
            print( i,end="")
    print()
print("=================================")

n=int(input("enter the number :"))
for i in range(n,(1-1),-1):
    for j in range(1,i+1):
            print( j,end="")
    print()
print("=================================")

n=int(input("enter the number :"))
for i in range(n,(1-1),-1):
    for j in range(n,i-1,-1):
            print(j,end="")
    print()
print("=================================")

n=int(input("enter the number :"))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
            print(j,end="")
    print()
print("=================================")

n=int(input("enter the number: "))
noc=1
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(j,end="")
    print()
    if i<n:
          noc+=1
    else:
          noc-=1
print("=================================")
'''
n=int(input("enter the number :"))
noc=n
for i in range(1,n*2):
    for j in range(n,noc+1):
            print(j,end="")
    print()
    if i<n:
          noc-=1
    else:
          noc+=1
