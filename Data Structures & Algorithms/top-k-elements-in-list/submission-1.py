"""
counts = dict() 
    (num: count)
    -1000: 10

((count, num), (count, num))

maxheap O(n)

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int) # { num: count }
        for num in nums:
            counts[num] += 1
        
        q = []
        for num, count in counts.items():
            heapq.heappush(q, (count, num))
            if len(q) > k:
                heapq.heappop(q)

        return [ n for _, n in q ]

        