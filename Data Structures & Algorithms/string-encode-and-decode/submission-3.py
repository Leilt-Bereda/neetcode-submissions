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
            while i < len(s) and s[i] != "#":
                i += 1
            length = int(s[j:i])
            j = i + 1
            res.append(s[j:length + j])
            i = length + j
            j = i
        return res