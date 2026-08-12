"""
[1,2,4,6] 

[]

[1,8,16,64]
[1,1,2,4]
[48,24,12,4]

len = 4


i from 1 to 3

nums = [1,2,4,6]
res = 1,1,2,8
res = 
2,1,0
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        accum = 1
        for i in range(1, len(nums)):
            accum = nums[i-1] * accum
            res[i] *= accum
        accum = 1
        for i in reversed(range(0, len(nums)-1)):
            accum = nums[i+1] * accum
            res[i] *= accum
        return res




                
        