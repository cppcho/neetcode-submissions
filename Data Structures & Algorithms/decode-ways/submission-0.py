"""
1012
1  -> 1
10 12 -> 1
10 1 2 -> 1

solve(start) # contract: num of way to decode it from start

ways = 0
for each prefix
    ways += solve(start + len(prefix)) 
return ways
    
check prefix(s): (True, length)

"""
class Solution:
    def numDecodings(self, s: str) -> int:
        prefixs = set()
        for i in range(1, 27):
            prefixs.add(str(i))
        memo = [-1] * len(s)
        def solve(start):
            if start == len(s):
                return 1
            if memo[start] > -1:
                return memo[start]
            res = 0
            if start <= len(s) - 1 and s[start:start+1] in prefixs:
                res += solve(start+1)
            if start <= len(s) - 2 and s[start:start+2] in prefixs:
                res += solve(start+2)
            memo[start] = res
            return res
            
        return solve(0)


            
            

        