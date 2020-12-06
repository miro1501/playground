"""
Runtime: 40 ms, faster than 54.39% of Python online submissions for Richest Customer Wealth.
Memory Usage: 13.4 MB, less than 52.54% of Python online submissions for Richest Customer Wealth.
"""

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        rtype = 0
        for i in range(len(accounts)):
            tmp = 0
            for j in range(len(accounts[i])):
                tmp += accounts[i][j]
            if tmp > rtype:
                rtype = tmp
        return rtype

#ccounts = [[1,2,3],[3,2,1]] #output 6
#accounts = [[1,5],[7,3],[3,5]] #output 10
accounts = [[2,8,7],[7,1,3],[1,9,5]] #output 17
rtype = Solution.maximumWealth(None, accounts)
print(rtype)