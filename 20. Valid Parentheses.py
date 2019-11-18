class Solution:
    def isValid(self, s: str) -> bool:
        
        
        stack = []
        
        mapping = { ')':'(' , '}':'{', ']':'['  }
        
        for bracket in s:
        
            if bracket in mapping:
                
                top_element = stack.pop() if stack else '#'
                
                if top_element != mapping[bracket]:
                    return False




            else:
                stack.append(bracket)
                
        
        return not stack