def createIntArray():
    l1=[]
    while True:
        try:
            n=int(input("enter a val: "))
            l1.append(n)
        except Exception as e:
            return l1
def seggregation(arr):
    dup,nondup,unique=[],[],[]
    dict={}
    for i in range(0,len(arr)-1):
        if arr[i] in dict:
            dict[arr[i]]+=1
        else:
            dict[arr[i]]=1
    for key,val in dict.items():
        if val >1:
            dup.append(key)
        if val>=1:
            nondup.append(key)
        if val==1:
            unique.append(key)
    return dup,nondup,unique
arr=createIntArray()
print("the original array :",arr)
resdup,resnondup,resunique=seggregation(arr)
print("duplicate : ",resdup)
print("non duplicate : ",resnondup)
print("unique elemenst: ",resunique)

