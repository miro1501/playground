def sort_two_list(nums):
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
        return nums
    
l1 = [1, 1, 2, 3]
l2 = [1, 2, 2, 3, 3]
new_num_list = l1 + l2

new_sorted_num_list = sorted(new_num_list)
#print(sorted(new_sorted_num_list)) 
print(sort_two_list(new_sorted_num_list))
