arr=[1,12,3,14,11,2,13,4,10]
def part(arr,left,right):
    i=left-1
    j=left
    p=arr[right-1]
    while j<=right-1:
        if arr[j]<=p:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    return i
def quicksort(arr,left,right):
    if left<right:
        x=part(arr,left,right)
        quicksort(arr,left,x-1)
        quicksort(arr,x+1,right)
    return arr

print(quicksort(arr,0,len(arr)))