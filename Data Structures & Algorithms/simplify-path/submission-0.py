class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        lst = path.split("/")
        for s in lst:
            if s == "..":
                if stack:
                    stack.pop()
            elif s != "" and s!= ".":
                stack.append(s)
        return "/" + "/".join(stack)

# path = "/neetcode/practice//...///../courses"

# lst = "",neetcode,practice,"",...,"","",..,courses
# stack = neetcode, practice,courses