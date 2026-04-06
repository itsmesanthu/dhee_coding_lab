def createIntArray():
    l1=[]
    while True:
        try:
            n=int(input("enter a val: "))
            l1.append(n)
        except Exception as e:
            return l1
def maregshort(arr1,arr2):
    res=[]
    i,j=0,0
    n1,n2=len(arr1),len(arr2)
    for k in range(0,(n1+n2)):
        if i<n1 and k%2==0:
            res.append(arr1[i])
            i+=1
        elif j<n2 and k%2!=0:
            res.append(arr2[j])
            j+=1
        else:
            if i<n1:
                res.append(arr1[i])
                i+=1
                k+=1
            elif j<n2:
                res.append(arr2[j])
                j+=1
                k+=1
    return res

def maregshort2(arr1,arr2):
    odd=1
    for j in range(0,len(arr2)):
        arr1.insert(odd,arr2[j])
        odd+=2

def twoasc(arr1,arr2):
    res=[]
    i,j=0,0
    n1,n2=len(arr1),len(arr2)
    for k in range(0,(n1+n2)):
            if i<n1 and j<n2:
                if arr2[j]<=arr1[i]:
                    res.append(arr2[j])
                    j+=1
                elif arr2[j]> arr1[i]:
                    res.append(arr1[i])
                    i+=1
            else:
                if i<n1:
                    res.append(arr1[i])
                    i+=1
                    k+=1
                elif j<n2:
                    res.append(arr2[j])
                    j+=1
                    k+=1
    return res
arr1=createIntArray()
print("array 1 is ",arr1)
arr2=createIntArray()
print("array 2 is ",arr2)
# res=maregshort(arr1,arr2)
# print(res)
# maregshort2(arr1,arr2)
# print(arr1)
res=twoasc(arr1,arr2)
print(res)