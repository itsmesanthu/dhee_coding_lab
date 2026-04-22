'''def createarray():
    print("enter the element to created array")
    l=[]
    while True:
        try:
            n=int(input("enter the element:"))
            l.append(n)
        except Exception as e:
            return l
def subarray(arr):
    for i in range(0,len(arr)):
        res=[]
        for j in range(i,len(arr)):
            res.append(arr[j])
            print(res)
arr=createarray()
print("oiginal array: ",arr)
subarray(arr)'''
def createarray():
    print("enter the element to created array")
    l=[]
    while True:
        try:
            n=int(input("enter the element:"))
            l.append(n)
        except Exception as e:
            return l
'''def subarray(arr):
    res=[]
    for i in range(0,len(arr)):
          for j in range(i,len(arr)):
            sub=[]
            for k in range(i,j+1):
                sub.append(arr[k])
            res.append(sub)
    return res'''
def subarray(arr):
    res=[]
    for i in range(0,len(arr)):
          for j in range(i,len(arr)):
            sub=[]
            sub=arr[i:j+1]
            res.append(sub)
            for i in range(0,len(sub)):
                sum=0
                sum=sum+sub[i]
                print(sum)
    return res
def maxSubArray(nums):
        cunsum=0
        maxsum=-2**31
        sub=[]
        for i in range(0,len(nums)):
            cunsum+=nums[i]
            h=nums[i]
            if cunsum>maxsum:
                sub.append[h]
                maxsum=cunsum
            if cunsum<0:
                cunsum=0
        print(sub)
        return maxsum

arr=createarray()
print("oiginal array: ",arr)
# sub=subarray(arr)
# print("the sub array is : ",sub)
se= maxSubArray(arr)
print(se)
