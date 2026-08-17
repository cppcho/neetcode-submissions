class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0: 1}
        curr_sum = 0
        res = 0
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum not in mp:
                mp[curr_sum] = 0

            tar = curr_sum - k
            if tar in mp:
                res += mp[tar]
            mp[curr_sum] += 1
            
        return res



        
    
