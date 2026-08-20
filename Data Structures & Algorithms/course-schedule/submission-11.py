"""
run each c
2 0 1, 1 0
0->

True 0->1, 1 -> 2, 0->2 
False 0->1, 1->2, 0->2 
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjs = dict()    # course num -> prereqs
        for pre in prerequisites:
            if pre[0] not in adjs:
                adjs[pre[0]] = list()
            adjs[pre[0]].append(pre[1])

        visiting = set()
        def dfs(i):
            if i in visiting: # loop
                return False

            visiting.add(i)
            if i in adjs:
                for adj in adjs[i]:
                    r = dfs(adj) 
                    if not r:
                        return False
                adjs[i] = []
            visiting.remove(i)
            return True


        for i in range(numCourses):
            r = dfs(i)
            if not r:
                return False
        
        return True



        