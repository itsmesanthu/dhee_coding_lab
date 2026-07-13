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
    print(arr)
    return i
res=part(arr,0,len(arr))
print(res)
part(arr,0,res-1)
part(arr,res+1,len)