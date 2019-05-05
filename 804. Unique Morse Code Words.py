import string
class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        s = ''
        d = {}
        alphab = list (string.ascii_lowercase)
        count = 0     
        t =  [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        zipbObj = zip(alphab, t)
        n = dict(zipbObj)
        
        for i in words:
            
            for j in i:
                
                s=s+n[j]
            d.update({i:s})
            s=''
            
        
        leng = len(d)
        
        uniqueTransformations = []
                   
        for value in d:
            if (d[value] not in uniqueTransformations):
                uniqueTransformations.append(d[value])
        
        return (len(uniqueTransformations))
        
A = Solution() 
A.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])       

        