class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = defaultdict(int)
        for ch in s1:
            counts[ch] += 1

        l = 0
        for r in range(len(s2)):
            # make the l and counts valid
            ch = s2[r]
            if ch in counts:
                counts[ch] -= 1
                while counts[s2[r]] < 0:
                    counts[s2[l]] += 1
                    l += 1
            else:
                while l < r:
                    counts[s2[l]] += 1
                    l += 1
                l = r + 1

            if r - l + 1 >= len(s1):
                return True
        return False




        