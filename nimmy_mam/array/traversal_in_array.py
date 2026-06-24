arr=[1,2,3,4,5]
# type of array traveral 
# 1 > liner traveral 
def liner_traveral(arr):
    for i in arr:
        print(i,end=" ")
    print()
print("liner traveral")
liner_traveral(arr)

#Reverse traveral
def Reverse_traveral(arr):
    for i in range(len(arr)-1,-1,-1):
        print(i,end=" ")
    print()
print("Reverse traveral")
Reverse_traveral(arr)

# methods of array traversal
  
    # 1) for loop
def for_loop(arr):
    for i in arr:
        print(i+1, end=" ")
    print()
print(" for loop")
for_loop(arr)

    #2) while loop
def  while_loop(arr):
    i,n=0,len(arr)
    while i<n:
        print(arr[i],end=" ")
        i+=1
    print()
print(" while loop")
while_loop(arr)

# application of array traversal 

    # 1) searching elements
def searching_elements(arr,target):
    for i in arr:
        if i==target:
            return True
print(" searching elements")
res=searching_elements(arr,3)
if res:
    print("element is found")
else:
    print("element is not found")
    # 1.1) searching elements if element is found print it index value and with statement "element  found at this index"
def index(arr,target):
    n=len(arr)
    for i  in range(0,n-1):
        if arr[i]==target:
            return i
s=int(input("enter the number : "))
flag=index(arr,s)
if flag:
    print(f"element {s} is  found at this index:{flag}")
else:
    print(f"element {s} is not found")

    # 2) modifying elements
def modifying(arr):
    for i in arr:
        print(i**2,end=" ")
    print()
modifying(arr)