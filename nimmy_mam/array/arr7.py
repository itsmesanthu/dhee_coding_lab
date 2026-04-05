'''#asending order binary search array
def createIntArray():
    l1=[]
    while True:
        try:
            n=int(input("enter a val: "))
            l1.append(n)
        except Exception as e:
            return l1
def binarySearchArray(arr,t):
    st,en=0,len(arr)-1
    while st<=en:
        m=(st+en)//2
        if t==arr[m]:
            return m
        if t <arr[m]:
            en=m-1
        else:
            st=m+1
    return -1
arr=createIntArray()
print(arr)
t=int(input("enter the finding number :"))
f=binarySearchArray(arr,t)
if f==-1:
    print(f"the {t} number is not found")
else:
    print(f"the {t} is founded in index is {f}")
#desending order binary search array
def createIntArray():
    l1=[]
    while True:
        try:
            n=int(input("enter a val: "))
            l1.append(n)
        except Exception as e:
            return l1
def binarySearchArray(arr,t):
    st,en=0,len(arr)-1
    while st<=en:
        m=(st+en)//2
        if t==arr[m]:
            return m
        if t <arr[m]:
            st=m+1
        else:
            en=m-1
    return -1
arr=createIntArray()
print(arr)
t=int(input("enter the finding number :"))
f=binarySearchArray(arr,t)
if f==-1:
    print(f"the {t} number is not found")
else:
    print(f"the {t} is founded in index is {f}")'''
def array():
    l=[]
    while True:
        try:
            n=int(input("enter the num:"))
            l.append(n)
        except Exception as e:
            return l
def binary(arr,t):
    st,en=0,len(arr)-1
    flag= "asc"
    if st>en:
        flag="desc"
    while st<=en:
        m=(st+en)//2
        if t==arr[m]:
            return m
        if flag=="asc":
            if t <arr[m]:
                en=m-1
            else:
                st=m+1
        else:
            if t <arr[m]:
                st=m+1
            else:
                en=m-1
    return -1
arr=array()
print(arr)
t=int(input("enter the finding number :"))
f=binary(arr,t)
if f==-1:
    print(f"the {t} number is not found")
else:
    print(f"the {t} is founded in index is {f}")           

