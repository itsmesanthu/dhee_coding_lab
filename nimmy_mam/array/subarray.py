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
        for i in range(0,len(nums)):
            cunsum+=nums[i]
            if cunsum>maxsum:
                maxsum=cunsum
            if cunsum<0:
                cunsum=0
        return maxsum

arr=createarray()
print("oiginal array: ",arr)
se= maxSubArray(arr)
print(se)
