"""
1. sort the array -> loop with single pointer 

seen to skip duplicate

----
thinking
- have a seen hash to remove duplicate
- assume no duplicate
[. . . . . . . . . . .]

0 -> (0, 0)
2 > (1, 6)
3 > (2, 3)

0 3 | looking for -1,1,2,4
[0] [3 2] | -1,1,4
[0] [3 2] [5] | -1,1,4,6                       
[0] [3 2] [5] | 4: seen 3 (2,3) before (=can join), seen 5 (5) before = can join
                    -> - (2,5)

prev and next not exist -> add (n, n)
prev and next both exist -> get min from prev and max from next, update min and max
on ly prev exist -> get min and max from prev 
{

}

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(list) # num -> current min max range (x, y)

        res = 0
        for num in nums:
            if num in mp:
                continue
            curr_min = num
            curr_max = num
            if num - 1 in mp:
                curr_min = mp[num-1][0]
            if num + 1 in mp:
                curr_max = mp[num+1][1]
            mp[curr_min] = [curr_min, curr_max]
            mp[curr_max] = [curr_min, curr_max]
            res = max(res, curr_max - curr_min + 1)
            
        return res

            
        



        