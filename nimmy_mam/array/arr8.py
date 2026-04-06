'''#33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
            s, e = 0, len(nums) - 1

            while s <= e:
                m = (s + e) // 2
                if target == nums[m]:
                    return m
                if nums[s] <= nums[m]:
                    if nums[s] <= target <= nums[m]:
                        e = m - 1
                    else:
                        s = m + 1
                else:
                    if nums[m] <= target <= nums[e]:
                        s = m + 1
                    else:
                        e = m - 1
            return -1
#852. Peak Index in a Mountain Array
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s,e=0,len(arr)-1
        while s<e:
            m=(s+e)//2
            if arr[m]<arr[m+1]:
                s=m+1
            else:
                e=m
        return s

'''
#merging array
a=[1,2,3,4]
b=[5,6,7,8,4]
print("extended")
a.extend(b)
print(a)
print(b)
print("+ concatenation")
c=a+b
print(c)
print(a)
print(b)
print("append")
a.append(b)
print(a)
print(b)
print("insert ")
a.insert(0,b)
print(a)
print(b)