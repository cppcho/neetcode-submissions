"""
blute force
O(n^2)

- foo(i, k) num of sub array start from index i, sum to k
    foo(i+1, k-nums[i])
- our solution = sum all i

1,2,3,4,5


2 1 2 4

2 -1 1 2

1 1 1 1 1 1

1 2 3 4 5 6
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(set)
        sums = []
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            sums.append(curr_sum)
            mp[curr_sum].add(i)

        res = 0
        for j in range(len(nums) - 1, -1, -1):
            tar = sums[j] - k
            if mp[tar]:
                for y in mp[tar]:
                    if y < j:
                        res += 1
            if tar == 0:
                res += 1
            
        return res



        
    
