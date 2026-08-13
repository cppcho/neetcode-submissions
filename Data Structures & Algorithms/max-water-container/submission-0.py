class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            res = max(res, self.calcArea(heights, l, r))

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                
        return res

    def calcArea(self, heights, left, right):
        return (right - left) * min(heights[left], heights[right])