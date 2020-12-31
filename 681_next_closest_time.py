class Solution:
    def nextClosestTime(self, time: str) -> str:        

        # convert time to minutes
        cur = int(time[:2])*60 + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        
        while True:
            # start incrementing time one by one and see if all digits present in allowed
            # however, we can't keep on incerasing...24*60 is the upper limit, so find mod of that
            cur = (cur + 1)%(24*60)
            
            if all(digit in allowed
                  for block in divmod(cur,60)
                   for digit in divmod(block,10)):
                return "{:02d}:{:02d}".format(*divmod(cur,60))
                
        
        
