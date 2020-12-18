"""
Runtime: 8 ms, faster than 99.79% of Python online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 13.7 MB, less than 13.48% of Python online submissions for Number of Steps to Reduce a Number to Zero.
"""

class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        rtype = 0
        while num > 0:    
            rtype += 1        
            tmp = num
            if (num % 2) == 0:                
                num = num // 2
                print("Step {}) {} is even; divide by 2 and obtain {}.".format(rtype, tmp, num))
            else: 
                num -= 1
                print("Step {}) {} is odd; substract 1 and obtain {}.".format(rtype, tmp, num))            
        return rtype
integer = 14 #output 6
integer = 8 #output 4
solution = Solution.numberOfSteps(None, integer)
print(solution)