class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rtype = False
        if (str(x) == str(x)[::-1]):
            rtype = True
            return rtype

class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return(str(x) == str(x)[::-1])

class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse_integer = 0
        iterator = 0

        if x < 0:
            return False

        while (x // (10 ** iterator) != 0):
            reverse_integer = (reverse_integer * 10 ) + (x // (10**iterator) % 10)
            iterator += 1
        
        return (x == reverse_integer)

        



integer = 121
solution = Solution.isPalindrome(None, integer)
print(solution)
solution1 = Solution1.isPalindrome(None, integer)
print(solution1)
solution2 = Solution2.isPalindrome(None, integer)
print(solution2)