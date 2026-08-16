class Solution:
    dp = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.dp = {}
        res = self.solve(s, wordDict, 0)
        return res

    def solve(self, s, wordDict, start):
        if start == len(s):
            return True
        if start > len(s):
            return False
        if start in self.dp:
            return self.dp[start]
        for word in wordDict:
            if s[start:].startswith(word):
               r = self.solve(s, wordDict, start + len(word))
               if r:
                    self.dp[start] = True
                    return True
        self.dp[start] = False
        return False