"""
3,4,5,6,7,1,2
    3 6 2 ->  1: smaller than 3 -> right half
              4: larger than 3 -> smaller than mid -> left
              7: larger than left and mid -> right half

1. left < right
    normal binary search
2. left > right
    rotated
        -> mid can be smaller / greater than both
        6,1,2,3,4,5 
        2,3,4,5,6,1

    mid == target end
        left < target < mid
        mid < right -> 


left mid right
"""
class Solution:
    # 0 1 2 mid = 1
    # 0 1 -> mid = 0
    # 0 -> mid 0
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right

            if nums[left] < nums[right]:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] < nums[mid]:
                    if nums[left] < target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[mid] < target < nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1







        