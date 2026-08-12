"""
sep = !0
! = !!

"hello!0world" -> hello!0world
"""
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            encoded = ""
            for ch in s:
                if ch == "!":
                    encoded += "!!"
                else:
                    encoded += ch
            res += encoded
            res += '!0'
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        pos = 0
        curr_str = ""
        while pos < len(s):
            ch = s[pos]
            if ch == '!':
                if pos+1 >= len(s):
                    raise RuntimeError("should not happen")
                next_ch = s[pos+1]
                if next_ch == '0':
                    res.append(curr_str)
                    curr_str = ""
                    pos += 1
                elif next_ch == '!':
                    curr_str += '!'
                    pos += 1
                else:
                    raise RuntimeError("should not happen")
            else:
                curr_str += ch
            pos += 1

        return res
