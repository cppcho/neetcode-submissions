"""
["act","pots","tops","cat","stop","hat"]
[""]
["x"]
["xxx", "xx"]

counts = dict() 
    "act" -> [0, 3]
    "aht" -> [5]
    ...
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for i, s in enumerate(strs):
            count = [0]*26
            for ch in s:
                count[ord(ch)-ord('a')] += 1
            counts[tuple(count)].append(s)

        return list(counts.values())


        
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for i, str in enumerate(strs):
            k = "".join(sorted(str))
            counts[k].append(i)

        result = []
        for indices in counts.values():
            group = []
            for i in indices:
                group.append(strs[i])
            result.append(group)

        return result
