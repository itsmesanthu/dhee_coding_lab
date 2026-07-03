    # insert an element  to the array.
arr=[1,2,3,4,5]
# nsert Element at the Beginning of an Array
#[Approach 1] Using Built-In Methods
    #insert method
def insert(arr,ele):
    arr.insert(0,ele)
    for i in arr:
        print(i,end=" ")
    print()
ele=int(input("enter inserting element:"))
insert(arr,ele)
# [Approach 2] Using Custom Method
    #silcing method
def silc(arr,ele):
    arr[0]=ele
    for i in arr:
        print(i,end=" ")
    print()
el=int(input("enter inserting element:"))
silc(arr,el)

# Insert Element at a Given Position in an Array
    #silcing method
def silc1(arr,ele,p):
    arr[p]=ele
    for i in arr:
        print(i,end=" ")
    print()
el=int(input("enter inserting element:"))
p=int(input("position of numbere:"))
silc1(arr,el,p)

    #insert method
def insert1(arr,ele,po):
    arr.insert(po,ele)
    for i in arr:
        print(i,end=" ")
    print()
ele=int(input("enter inserting element:"))
po=int(input("entre the posion:"))
insert1(arr,ele,po)

def appen(arr,ele):
    arr.append(ele)
    for i in arr:
        print(i,end=" ")
    print()
n=int(input("enter the element : "))
appen(arr,n)