'''n=input("enter the number:")
print(type(n))
print(n)
print("=======================")

#an exception is occured when "" is inserted
try:
    n=input("enter the number:")
    print(type(n))
    print(n)
except Exception as e:
    print("invalid")'''

'''
def creatarray():
    print("enter the elements into the array to be created :")
    l1=[]
    while True:
        try:
            n=int(input("enter a element: "))
            l1.append(n)
        except Exception as e:
            return l1
arr=creatarray()
print("original array is :",arr)
print("====================================")'''

'''def creatarray():
    print("enter the elements into the array to be created :")
    l1=[]
    while True:
        n=input("enter a element: ")
        if n=="":
            return l1
        l1.append(n)
 
arr=creatarray()
print("original array is :",arr)
print("====================================")'''

''''def indexnum(arr, num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    return -1
arr=[5,6,16,-90,23,5,23,85]
num=23
index=indexnum(arr,num)
if index !=1:
    print("")
print("====================================")'''

'''def creatarray():
    print("enter the elements into the array to be created :")
    l1=[]
    while True:
        try:
            n=int(input("enter a element: "))
            l1.append(n)
        except Exception as e:
            return l1
arr=creatarray()
target=int(input("enter the element to find:"))
flag,index=False,-1
for i in range(0,len(arr)):
    if target==arr[i]:
        flag=True
        index=i
        break
print("original array : ",arr)
if flag:
    print(f"the {target} element is found at index:{index}")
else:
    print(f"{target} element not found ")
print("====================================")'''

'''def creatarray():
    print("enter the elements into the array to be created :")
    l1=[]
    while True:
        try:
            n=int(input("enter a element: "))
            l1.append(n)
        except Exception as e:
            return l1

def indexnum(arr, target):
    #flag,index=False,-1
    for i in range(0,len(arr)):
        if arr[i]==target:
            return True, i
    return False,-1
arr=creatarray()
target=int(input("enter the element to find:"))
flag,index=indexnum(arr,target)
if flag:
    print(f"the {target} element is found at index:{index}")
else:
    print(f"{target} element not found ")
print("================================")'''

def creatarray():
    print("enter the elements into the array to be created :")
    l1=[]
    while True:
        try:
            n=int(input("enter a element: "))
            l1.append(n)
        except Exception as e:
            return l1

def diffarray(arr):
    sum,pord=0,1
    diff=0
    for i in range(0,len(arr)):
        pord=pord*arr[i]
        sum= sum+arr[i]
    diff=pord-sum
    if diff<0:
        diff*=-1
    return diff
arr=creatarray()
d=diffarray(arr)
print("array diff. is :",d)