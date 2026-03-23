#butterfly pattren:
n=int(input("enter the number:"))
noc, nor=1,((n*2)-1)
for i in range(1,(n*2)):
    for j in range(1,(n*2)):
        if j<=noc or j>=nor:
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

n=int(input("enter the number :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("=================================")

n=int(input("enter the number :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==j or (i+j)==(n+1):
               print("*",end=" ")
        else:
               print(" ",end=" ")
    print()

print("=================================")

n=int(input("enter the number :"))
if n%2==0:
     n=n+1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==j or (i+j)==(n+1):
               print("*",end=" ")
        else:
                print(" ",end=" ")
    print()
print("=================================")

n=int(input("enter the number :"))
if n%2==0:
     n=n+1
for i in range(1,n+1):
    for j in range(1,n+1):
        if   j==1 or j==n or i==j or (i+j)==(n+1):
               print("*",end=" ")
        else:
                print(" ",end=" ")
    print()
print("=================================")

n=int(input("enter the number :"))
if n%2==0:
     n=n+1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or i==j or (i+j)==(n+1):
               print("*",end=" ")
        else:
                print(" ",end=" ")
    print()

print("=================================")

n = int(input("enter a num: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == n or j == 1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("=================================")


n = int(input("enter a num: "))

for i in range(1, n + 1):
    for k in range(n, i, -1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
