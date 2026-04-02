def createIntArray():
    l1=[]
    while True:
        try:
            n=int(input("enter a val: "))
            l1.append(n)
        except Exception as e:
            return l1
# def bubblesort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
# arr=createIntArray()
# print("orignal array",arr)
# bubblesort(arr)
# print("Ascsorted array",arr)
 
# def insertion(arr):
#     n=len(arr)
#     for i in range(0,(n-1)):
#         for j in range(i+1,0,-1):
#             if arr[i]>arr[j]:
#                 arr[j-1],arr[j]=arr[j],arr[i]
#             else:
#                 break

# insertion(arr)
# print("asc sorted array",arr)
def reverseArray(arr):
    l=[]
    for i in range(len(arr)-1,0-1,-1):
        l.append(arr[i])
    return l

def arrayreve(arr):
    i,j=0,len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

arr=createIntArray()
arrayreve(arr)
print("hi",arr)
hi=reverseArray(arr)
print("the reverse os give array:",hi)
