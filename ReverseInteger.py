class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        posFlag = 1
        limit = (2 ** 31) - 1
        if x < 0:
            posFlag = -1
            limit = 2 ** 31
            x = x * -1
        newNum = 0
        while x != 0:
            newNum = (newNum * 10) + (x%10)
            x = x//10
            if(newNum > 2**31):
                newNum = 0
                break
        return newNum * posFlag
