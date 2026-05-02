# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.

# Sample variables to test the function
nums = [3,3]
target = 6

def twoSum(nums, target):
   # Init a list variable to append the indices
   indices_list = []

   # Iterate the list with index.
   for i,num in enumerate(nums):
      # For each number, calculate the target number
      a = target - num
      # Check if target is present in the next slice of list. Dont include current index.
      if a in nums[i+1:]:
         # If target is present, append current index and target index into the return list
         indices_list.append(i)
         indices_list.append(nums.index(a, i+1))

   return indices_list

print(twoSum(nums, target))


