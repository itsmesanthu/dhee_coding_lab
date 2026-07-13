def sortArray(nums):
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if  nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
    return nums
arr=[10,7,6,5,20,-1,-2]
print(sortArray(arr))