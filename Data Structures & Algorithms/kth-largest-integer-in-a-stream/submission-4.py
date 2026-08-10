class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.nums = nums
        self.k = k
        pass
        

    def add(self, val: int) -> int:
        if len(self.nums) > 0 and val <= self.nums[0]:
            return self.nums[0]
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

if __name__ == "main":
    kthLargest = KthLargest(3, [1, 2, 3, 3])
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(6))
    print(kthLargest.add(7))
    print(kthLargest.add(8))
        
