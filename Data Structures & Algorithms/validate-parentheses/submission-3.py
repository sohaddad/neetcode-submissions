class Solution:
    def isValid(self, s: str) -> bool:
        stack_ = []
        for char in s:
            if char in ['(', '{', '[']:
                stack_.append(char)
            elif stack_ and ((char == ')' and stack_[-1] == '(') or 
                             (char == '}' and stack_[-1] == '{') or 
                             (char == ']' and stack_[-1] == '[')):
                stack_.pop()
            else:
                return False
        if len(stack_) == 0:
            return True
        return False    
