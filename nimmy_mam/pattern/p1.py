print("*")
print("==============================")


n=int(input("enter the number: "))
for i in range(n): #i represent the row
    print("*")
print("==============================")


n=int(input("enter the number: "))
for j in range(n):# j represent coloumn
    print("*" ,end=" ")
print("\n==============================")

n=int(input("enter the number : "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print("\n==============================")

n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()