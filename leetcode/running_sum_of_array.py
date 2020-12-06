"""
Runtime: 24 ms, faster than 78.83% of Python online submissions for Running Sum of 1d Array.
Memory Usage: 13.7 MB, less than 38.32% of Python online submissions for Running Sum of 1d Array.
"""
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rtype = []
        next_index = 0
        for i in range(len(nums)):
            if i == 0:
                rtype.append(nums[0])
            else:     
                tmp = rtype[i-1] + nums[next_index]                
                rtype.append(tmp)
                
            next_index = next_index + 1
        return rtype

"""
Runtime: 28 ms, faster than 54.34% of Python online submissions for Running Sum of 1d Array.
Memory Usage: 13.6 MB, less than 38.32% of Python online submissions for Running Sum of 1d Array.
"""
class Solution1:
    def runningSum(self, nums):
        rtype=[]
        tmp=0
        for i in nums:
            tmp+=i
            rtype.append(tmp)
        return rtype

#l1 = []
#l1 = [1,2,3] # output [1, 3, 6]
#l1 = [1,2,3,4] # output [1, 3, 6, 10]
#l1 = [1,1,1,1,1] # output [1, 2, 3, 4, 5]
l1 = [3,1,2,10,1] # output [3, 4, 6, 16, 17]
solution = Solution1.runningSum(None, l1)
print(solution)
