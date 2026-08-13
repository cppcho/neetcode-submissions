"""
[1,2,3,4] 3
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                break
            elif curr_sum > target:
                right -= 1
            else:
                left += 1

        if left >= right:
            raise Exception("should not happen here")

        return [left + 1, right + 1]
        
        