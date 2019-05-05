class Solution:
    def numUniqueEmails(self, emails) -> int:

        s = ''
        c = 0
        f=[]
        foundAt = 0
        foundPlus = 0
        foundDot = 0
        t =[]
        for k in range (0, (len(emails))):
            for i in emails[k]:
                
                if (i == '@'):
                    foundAt = 1
                 #   s = s + i
                elif (i == '.'):
                    foundDot = 1
                      
                #elif (i == '.' and foundAt == 1):
                    #foundDot = 0
                ##    s = s+i
                elif (i == '+'):   
                    foundPlus = 1
                #elif (i == '+' and foundAt == 1):
                 #   foundPlus = 1
                    
                
                
                
                    
                    
                if (foundPlus == 0 and foundAt == 0 and foundDot == 0):
                    s = s + i
                elif (foundPlus == 0 and foundAt == 0 and foundDot == 1):
                    foundDot = 0  
                    continue
                
                elif (foundPlus == 0 and foundAt == 1 and foundDot == 0):
                    s = s + i
                elif (foundPlus == 0 and foundAt == 1 and foundDot == 1):
                    s = s + i        
                elif (foundPlus == 1 and foundAt == 0 and foundDot == 0):
                    continue
                elif (foundPlus == 1 and foundAt == 0 and foundDot == 1):
                    continue
                elif (foundPlus == 1 and foundAt == 1 and foundDot == 0):
                    s = s + i
                elif (foundPlus == 1 and foundAt == 1 and foundDot == 1):
                    s = s + i  
                    
            foundAt = 0
            foundPlus = 0
            foundDot = 0      
                    
             
                    
            
            
            f.append(s)
            s=''
            
            
       
        
        
        for h in f:
            
            if h not in t:
                t.append(h)
        return (len(t))
        #print(t)
                
        #print (c )        



A = Solution()
A.numUniqueEmails(["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"])