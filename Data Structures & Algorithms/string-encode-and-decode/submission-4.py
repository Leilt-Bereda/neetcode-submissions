'''
["Hello","World"]
5#Hello5World
l = 5
hello, world
["#0"]
2##0
l = 1
0
'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i < len(s):
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            j = i + 1
            res.append(s[j:length + j])
            i = length + j
            j = i
        return res

