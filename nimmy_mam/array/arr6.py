#rotation
#left rotation
'''def createIntArray():
    l1=[]
    while True:
        try:
            n=int(input("enter a val: "))
            l1.append(n)
        except Exception as e:
            return l1
def arrayreve(arr,i,j):
    # i,j=0,len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
def leftrotatoin(arr,k):
    n=len(arr)
    if k >=n:
        k=k%n
    arrayreve(arr,0,(k-1))

    arrayreve(arr,k,n-1)

    arrayreve(arr,0,n-1)
arr=createIntArray()
k=int(input("enter the number of rotations :"))
print("origin array : ",arr)
leftrotatoin(arr,k)
print("rotated array : ", arr)'''
#right rotation
'''def createIntArray():
    l1=[]
    while True:
        try:
            n=int(input("enter a val: "))
            l1.append(n)
        except Exception as e:
            return l1
def arrayreve(arr,i,j):
    # i,j=0,len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
def rightrotatoin(arr,k):
    n=len(arr)
    if k >=n:
        k=k%n
    arrayreve(arr,0,n-1)
    arrayreve(arr,0,(k-1))
    arrayreve(arr,k,n-1)
arr=createIntArray()
k=int(input("enter the number of rotations :"))
print("origin array : ",arr)
rightrotatoin(arr,k)
print("rotated array : ", arr)'''
# given array are palindrome 
def createIntArray():
    l1=[]
    while True:
        try:
            n=int(input("enter a val: "))
            l1.append(n)
        except Exception as e:
            return l1
def palindrome(arr):
    i,j=0,len(arr)-1
    while i<j:
        if arr[i]==arr[j]:
            i+=1
            j-=1
        else:
            return False
    return True
arr=createIntArray()
print(arr)
f=palindrome(arr)
if f :
    print("give the array is palinderome")
else:
    print("give array is not palinderome")