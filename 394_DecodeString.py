class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        # 
        for i in range (len(s)):
            
            if s[i]=="]":
                
                decodedString = []
                print("stack")
                print(stack)
                while(stack[-1]!='['):
                    decodedString.append(stack.pop())
                
                stack.pop()
                
                
                # pop until the [
                
                # then find k
                k = 0
                base = 1
                
                while stack and stack[-1].isdigit():
                    k += int(stack.pop())*base
                    base*=10
                
                
                
                # psush the number of times of k the decode word
                while k != 0:
                    for i in range(len(decodedString)-1,-1,-1):
                        stack.append(decodedString[i])
                    k-=1
                
            else:
                stack.append(s[i])
            
                
        return "".join(stack)
        
    
        


        
        
