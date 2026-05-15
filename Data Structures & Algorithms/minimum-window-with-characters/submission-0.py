'''
we have 2 edge cases:
    if s = "", return ""
    if len(s) < len(t): return ""
create 2 hashmaps:
    countT: to keep track of the characters that we need in t, which tells us the char that we need in the substring of s
    second one(window map): help us determine the char that we currently have
initialize 2 var:
    have: set to 0 first that tracks number of char in the current window that satisfies what we need
    need: set to the length of t's hashmap which tells us the char that we need
iterate thru s starting from 0 to len(s):
    maintain a hashmap for the current window
    if the current char is in countT and the value matches: increment have
    while our window is valid(have = need):
        - first: the window is valid right now, so record it
         next: then remove the left character
         after that: then check whether removing it made the window invalid
BOTTOM LINE: keep extending your window until we find a valid one and once we have that 
shrink it to see if we can find a shorter substring

'''
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or len(s) < len(t):
            return ""
        countT = defaultdict(int)
        window_map = defaultdict(int)
        for c in t:
            countT[c] += 1
        need = len(countT)
        have = 0
        resLen = float("infinity")
        res = ""
        l = 0
        for r in range(len(s)):
            window_map[s[r]] += 1
            if s[r] in countT and window_map[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                #as soon as we enter this while loop the window is valid so we need to record the length before we shrink it
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                    
                #remove left most char
                window_map[s[l]] -= 1
                #decrement have when the character is less than what is required
                #check if the char we removed made the window invalid
                if s[l] in countT and window_map[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return res




        