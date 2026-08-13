class Solution:
    """
    left,right = 0, 0 -> mid = 0
    left,right = 0, 1 -> mid = 0
    left,right = 0, 2 -> mid = 1
    """
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1
        