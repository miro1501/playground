nums = [1,1,2,2,3,3,4]
next_index = 1
index = 0
while index < len(nums):
    if nums[index] != nums[next_index]:
        nums[next_index] = nums[index]
        nums.pop(index)        
        index = index + 1
    else:
        nums.pop(index)  
        index = index + 1          
    next_index = next_index + 1    
    index = index + 1
    print("-> nums ", nums)
print(nums)