class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1=int(a,2)
        b1=int(b,2)
        c=a1+b1
        return bin(c)[2:]
        # return bin(int(a,2)+int(b,2))[2:]