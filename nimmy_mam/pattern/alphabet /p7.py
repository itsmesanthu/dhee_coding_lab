'''print(ord("A"))
print(ord(" "))
print(ord("8"))
#print(ord(""))#error
#print(ord("ee"))#error
print(chr(89))
print(chr(1234))
print(chr(00))
#print(chr(-23))#ValueError: chr() arg not in range(0x110000)
print("===============================")

n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(96+j),end="")
    print()
print("===============================")

n=int(input("enter the number : "))
for i in range(n,(1-1),-1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()
print("===============================")

n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2==0:
            print(chr(64+j),end="")
        else:
            print(chr(96+j),end="")
    print()'''
print("===============================")


n=int(input("enter the number : "))
for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):
        if j%2==0:
            print(chr(64+j),end="")
        else:
            print(chr(96+j),end="")
    print()
print("===============================")


n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2==1 and j%2==0 or i%2==0 and j%2==1:
            print(chr(64+j),end="")
        else:
            print(chr(96+j),end="")
    print()
print("===============================")

n=int(input("enter the number : "))
count=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2!=0:
            print(chr(64+count),end="")
            count+=1
        else:
            print(chr(96+count),end="")
            count+=1
    print()
print("===============================")

n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==4 or j==4:
            print(chr(96+n),end="")
        else:
            print(" ",end="")
    print()
print("===============================")

n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            print(chr(96+n),end="")
        else:
            print(" ",end="")
    print()

print("===============================")

n=int(input("enter the number : "))
noc=n
nor=1
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(chr(96+nor),end="")
    print()
    if i<n:
        noc-=1
        nor+=1
    else:
        noc+=1
        nor-=1
print("===============================")

n=int(input("enter the number : "))
noc=1
nor=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(chr(64+nor),end="")
    print()
    if i<n:
        noc+=1
        nor-=1
    else:
        noc-=1
        nor+=1