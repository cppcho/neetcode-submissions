"abcdazd"
"a0000abcd"
"0000"
"abcdefghijklmaz"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        right = 0
        mp = dict()

        for right in range(len(s)):
            # inv: left <= right < len(s)
            ch = s[right]
            if ch in mp:
                left = max(left, mp[ch] + 1)
            mp[ch] = right

            # inv s[left:right+1] does not contains non unique char
            res = max(res, right - left + 1)

        return res
        