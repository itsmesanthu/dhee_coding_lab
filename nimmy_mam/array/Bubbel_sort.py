arr=[]
def bubbel_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
res=bubbel_sort(arr)
print(res)