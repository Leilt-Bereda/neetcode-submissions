class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(sub):
            i = 0
            j = len(sub) -1
            while i < j:
                if sub[i] == sub[j]:
                    i += 1 
                    j -= 1 
                else:
                    return False
            return True
        n = len(s)
        count = 0
        for i in range(n):
            substring = ""
            for j in range(i, n):
                substring += s[j]
                if isPalindrome(substring):
                    count += 1
        return count
        