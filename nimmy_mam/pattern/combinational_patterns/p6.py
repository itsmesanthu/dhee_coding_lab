'''n=int(input("enter the number : "))
for i in range(n,(1-1),-1):
    for j in range(i,(1-1),-1):
        print(j,end="")
    print()
print("============================")

n=int(input("enter the number:"))
noc=1
for i in range(1,n*2):
    for j in range(noc,n+1):
        print(j,end="")
    print()
    if i<n:
          noc+=1
    else:
          noc-=1
print("==============================")

n=int(input("entern the number :"))
for i in range(1,n+1):
    for j in range(i,n+i):
        print(j,end="")
    print()
print("==============================")

n=int(input("entern the number :"))
for i in range(n,(1-1),-1):
    for j in range(i,n+i):
        print(j,end="")
    print()
print("==============================")

n=int(input("enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if(i+j)%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()
print("==============================")

n=int(input("enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j)%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()
print("==============================")'''

n=int(input("enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i <j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
print("==============================")

n=int(input("enter the number: "))
for i in range(n,(1-1),-1):
    for j in range(n,(1-1),-1):
        if i <j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
print("==============================")

n=int(input("enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i >j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
print("==============================")

n=int(input("enter the number: "))
for i in range(n,(1-1),-1):
    for j in range(n,(1-1),-1):
        if i >j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
print("======================")

n=int(input("enter the number: "))
count=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(count,end="")
        count+=1
    print()