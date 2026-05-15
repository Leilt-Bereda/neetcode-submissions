'''
ab   abbxxc

'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        reversedStr = ""
        while l < len(word1) and r < len(word2):
            reversedStr += word1[l]
            reversedStr += word2[r]
            l +=1
            r += 1
        while l < len(word1):
            reversedStr += word1[l]
            l += 1
        while r < len(word2):
            reversedStr += word2[r]
            r += 1
        return reversedStr