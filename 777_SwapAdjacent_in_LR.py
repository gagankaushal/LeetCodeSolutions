class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.count('X') != end.count('X'):
            return False
        
        sP = 0
        eP = 0
 
        sLength = len(start)
        eLength = len(end)
        
        while sP<sLength and eP<eLength:
            
            # get ahead of all X
            while sP<sLength and start[sP]=='X':
                sP+=1
            while eP<eLength and end[eP]=='X':
                eP+=1
            
            if sP==sLength or eP==eLength:
                return sP==sLength and eP==eLength
            
            if start[sP] != end[eP]:
                return False
            if start[sP]=='L' and sP<eP:
                return False
            if start[sP]=='R' and sP>eP:
                return False
            sP+=1
            eP+=1
        return True
            
