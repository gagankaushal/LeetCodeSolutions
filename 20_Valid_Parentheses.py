class Solution:
    def isValid(self, s: str) -> bool:
        
        # keep piushing in tack if opening bracket
        
        # pop only if key is the actual of closing else fasle
        
        
        stack = []
        
        brackets = {'{':'}','[':']','(':')'}
        
        for character in s:
            if character in brackets:
                stack.append(character)
                
            # elif character in brackets.values():
            else:
                if stack and brackets[stack.pop()] == character:
                    continue
                else:
                    return False
        # to make sure that stack is empty, only then we return true
        return not stack
        # print(stack)
        
