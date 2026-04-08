def createIntArray():
    l1=[]
    while True:
        try:
            n=int(input("enter a val: "))
            l1.append(n)
        except Exception as e:
            return l1
def mergesortmergin(arr,start,mid,end):
    i,j=start,mid+1
    res=[]
    for k in range(0,((mid+end)+1)):
        if i<=mid and j<=end:
            if arr[i]<=arr[j]:
                res.append(arr[i])
                i+=1
            else:
                res.append(arr[j])
                j+=1
        else:# for extar value
            if i<=mid:
                res.append(arr[i])
                i+=1
                k+=1
            elif j<=end:
                res.append(arr[j])
                j+=1
                k+=1
    #updating the original memory from res[]
    for k in range(0,len(res)):
        arr[start]=res[k]
        start+=1
def mergesortdivision(arr,start,end):
    if start>=end:
        return
    mid=(start+end)//2
    #LHS division
    mergesortdivision(arr,start,mid)
    #RHS division
    mergesortdivision(arr,mid+1,end)
    mergesortmergin(arr,start,mid,end)

arr=createIntArray()
print("orignal array :",arr)
mergesortdivision(arr,0,(len(arr)-1))
print("asc sored arr: ", arr)