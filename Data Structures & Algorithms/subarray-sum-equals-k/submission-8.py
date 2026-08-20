"""

k 2
    2 -1 1 2  prefix sum array
a:0 2 1 2
r:0 1 1 
t: a-2

memo  0:1 2:1 1:1


"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = defaultdict(int)  # accumlated_sum -> num of count
        memo[0] = 1
        accumlated_sum = 0
        res = 0
        for n in nums:
            accumlated_sum += n  # acc[i]
            target = accumlated_sum - k
            res += memo[target]
            memo[accumlated_sum] += 1
        return res


            



        
        