class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ("(", "{", "[")
        pairs = {")" : "(", 
                "}" : "{",
                "]" : "["}
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if not stack or stack.pop() != pairs[i]:
                    return False
        return not stack

