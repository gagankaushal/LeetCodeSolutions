class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        Address = ''
        
        k = 0
        for i in address:

            if i !='.':
                Address=Address+i

           elif i== '.':
                Address=Address+'['
                Address=Address+i
                Address=Address+']'
            
            
        return (Address)