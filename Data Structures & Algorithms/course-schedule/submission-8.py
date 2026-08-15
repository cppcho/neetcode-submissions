"""
for each num course
    check if there are any cycle

cycle -> false

seen 

1 -> 2  -> 4
  -> 3  -> 

1 -> 2 <-> 3

1 -> 2 -> 3
     ^
     |
     4 

9 -> 3 -> 5

[0, 2]

0 1 -> 3 9 -> 0 -> 3
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list) # from(int) -> to(list)
        for pre in prerequisites:
            a, b = pre
            mp[a].append(b)

        visiting = set()

        def dfs(n):
            if n in visiting:
                return False
            visiting.add(n)
            for adj in mp[n]:
                r = dfs(adj)
                if not r:
                    return False
                mp[n] = []
            visiting.remove(n)
            return True
            
        
        for n in range(numCourses):
            r = dfs(n)
            if not r:
                return False

        return True




        