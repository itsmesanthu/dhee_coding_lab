class Solution:
    def findPages(self, arr, k):
        if k>len(arr):
            return -1
        i=max(arr)
        j=sum(arr)
        while i<=j:
            m=i+(j-i)//2
            stu=1
            p=0
            for a in arr:
                if p+a>m:
                    stu+=1
                    p=a
                else:
                    p+=a
            if stu<=k:
                j=m-1
            else:
                i=m+1
        return i
obj=Solution()
arr=[12, 34, 67, 90]
k=2
print(obj.findPages(arr,k))
