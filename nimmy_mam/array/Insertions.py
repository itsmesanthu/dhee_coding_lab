    # insert an element  to the array.
arr=[1,2,3,4,5]
# 1)Insert Element at the Beginning of an Array
    #insert method
def insert(arr,ele):
    arr.insert(0,ele)
    for i in arr:
        print(i,end=" ")
    print()
ele=int(input("enter inserting element:"))
insert(arr,ele)
    #silcing method
def silc(arr,ele):
    arr[0]=ele
    for i in arr:
        print(i,end=" ")
    print()
el=int(input("enter inserting element:"))
silc(arr,el)
def appen(arr,ele):
    arr.append(ele)
    for i in arr:
        print(i,end=" ")
    print()
n=int(input("enter the element : "))
appen(arr,n)