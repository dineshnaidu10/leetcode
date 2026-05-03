# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:

#     nums1.length == m
#     nums2.length == n
#     0 <= m <= 1000
#     0 <= n <= 1000
#     1 <= m + n <= 2000
#     -106 <= nums1[i], nums2[i] <= 106

nums1 = [0,0,0,0,0]
nums2 = [-1,0,0,0,0,0,1]


def findMedianSortedArrays(nums1, nums2):

    def median_calc(num_list):
        if len(num_list) % 2 != 0:
            return num_list[len(num_list)//2]
        else:
            mid_1 = num_list[len(num_list)//2]
            mid_2 = num_list[len(num_list)//2 - 1]
            return (mid_1 + mid_2)/2
        
    if nums1 == []:
        return median_calc(nums2)
    elif nums2 == []:
        return median_calc(nums1)

    subtract_counter = 0
    action = True
    while action:
        num_target = nums2[0] - subtract_counter
        if num_target in nums1:
            index = nums1.index(num_target) + 1
            list_3 = nums1[:index] + nums2 + nums1[index:]
            action = False
        else:
            subtract_counter += 1
    
    return median_calc(list_3)

print(findMedianSortedArrays(nums1, nums2))



