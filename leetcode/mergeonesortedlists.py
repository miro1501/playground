#input [1,1,2,2,3,3,4]
#output [1,2,3,4]
#nums = [1,1,2,2,3,3,4]
nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]
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