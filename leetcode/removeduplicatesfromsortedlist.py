#input [1,1,2,2,3,3,4]
#output [1,2,3,4]

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        next_index = 1
        index = 0
        while index < len(nums):
            if nums[index] != nums[next_index]:
                next_index = next_index + 1    
                index = index + 1            
            else:
                nums.pop(index)  
            if next_index >= len(nums):
                break
        print(nums)
        return len(nums)

#nums = [1,1,2,2,3,3,4]
#nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5]
nums = []
rtype = Solution.removeDuplicates(None, nums)
print(rtype)