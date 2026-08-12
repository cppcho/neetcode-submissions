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
            q.append((-count, num))

        heapq.heapify(q) # O(n)

        res = []
        for _ in range(k):
            _, num = heapq.heappop(q)
            res.append(num)

        return res

        