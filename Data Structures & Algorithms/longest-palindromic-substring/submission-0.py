'''
s = "ababd"
Outer loop picks a starting point (i)

Inner loop extends the substring one character at a time (j)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""
        
        def isPalindrome(sub):
            i = 0
            j = len(sub) - 1

            while i < j:
                if sub[i] == sub[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        for i in range(n):
            substring = ""
            for j in range(i, n):
                substring += s[j] #keeps adding the next character to form all substrings starting from that position.
                if isPalindrome(substring):
                    if len(substring) > len(longest):
                        longest = substring
        return longest
        
