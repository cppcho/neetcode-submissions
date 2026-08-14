"""
XYYX k = 1
XXYX
XYXX

XYYY  k = 1 


- how to know which char to replace
- where to replace
- how to calculate the longest length
- blute force
    from index 0 X -> rright replace k, skip X -> get max length
    repeat


----
create set of chars and their first occurance

left, right
while right < len(s)
    move right ++ until k budget finish
    store length
    update the left

a, b
AABABBA

left=0,right=0,count=0
    count = 0
    res = 1
    right = 1
left=0,right=1,count=0
    count = 0
    res = 2
    right = 2
left=0,right=2,count=0
    count = 1
    res = 3
    right = 3 
left=0,right=3,count=1
    res = 4
left=0,right=4,count=1

AABA

AABABBA
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # cond: window - most freq key <= k
        count = defaultdict(int)
        l = 0
        maxf = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


    def characterReplacement2(self, s: str, k: int) -> int:
        res = 0
        st = set(s)
        for ch in st:
            left, right = 0, 0
            count = 0
            while right < len(s):
                # inv: left right always valid here
                if s[right] != ch:
                    if count < k:
                        count += 1
                    else:
                        while s[left] == ch:
                            left += 1
                        left += 1

                res = max(res, right-left+1)

                ## move pointer
                right += 1

        return res
                
        