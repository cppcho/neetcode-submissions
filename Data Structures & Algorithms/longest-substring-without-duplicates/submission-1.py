"abcdazd"
"a0000abcd"
"0000"
"abcdefghijklmaz"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        right = 0
        seen = set()
        while right < len(s):
            # inv: left <= right < len(s)
            ch = s[right]
            if ch in seen:
                while s[left] != ch:
                    seen.remove(s[left])
                    left += 1
                left += 1
            seen.add(ch)

            # inv s[left:right+1] does not contains non unique char
            res = max(res, right - left + 1)
            right += 1

        return res
        