#LHS inverted  rigth angular triangle
n=int(input("enter the number : "))
for i in range(n,(1-1),-1):
    for j in range(1,(i+1)):
        print("*",end=" ")
    print()
print("=============================")

#RHS rigth angular triangle
n=int(input("enter the number :  "))
for i in range(1,(n+1)):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,(i+1)):
        print("*",end="")
    print()
print("=============================")

#pyramid
n=int(input("enter the number :  "))
for i in range(1,(n+1)):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,(i+1)):
        print("* ",end="")
    print()
print("=============================")

#special pyramid
n=int(input("enter the number :  "))
for i in range(1,(n+1)):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,(i*2)):
        print("*",end="")
    print()
print("=============================")

#RHS inverted rigth angular tringle
n=int(input("enter the number:  "))
for i in range(n,1-1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
print("=============================")

#inverted pyramid
n=int(input("enter the number:  "))
for i in range(n,1-1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()
print("=============================")

#special inverted pyramid
n=int(input("enter the number:  "))
for i in range(n,1-1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i*2):
        print("*",end="")
    print()
print("=============================")

#LHS parallelogrom
n=int(input("enter the number:  "))
for i in range(n,1-1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")
    print()
print("=============================")

#RHS parallelogrom
n=int(input("enter the number:  "))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")
    print()