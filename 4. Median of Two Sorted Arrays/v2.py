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

nums1 = [3,2]
nums2 = [4,1]

def findMedianSortedArrays(nums1, nums2):

    # Function to return the median of a sorted list
    def median_calc(num_list):
        if len(num_list) % 2 != 0:
            return num_list[len(num_list)//2]
        else:
            mid_1 = num_list[len(num_list)//2]
            mid_2 = num_list[len(num_list)//2 - 1]
            return (mid_1 + mid_2)/2

    # Function to implement a Quick Sort algorithm
    def quicksort(arr):
        # If list's length is less than or equal 1, it is sorted by default
        if len(arr) <= 1:
            return arr

        # Choose the middle number as pivot
        pivot = arr[len(arr)//2]
        # Everything smaller than the pivot is put on a left list
        left = [x for x in arr if x < pivot]
        # Any number that is equal to pivot remains in a middle list
        middle = [x for x in arr if x == pivot]
        # Everything larger than the pivot is put on a right list
        right = [x for x in arr if x > pivot]

        # Call a recursive function by adding left, middle and right
        return quicksort(left) + middle + quicksort(right)

    # Create a new sorted list by inputting the sum of 2 input lists in the quicksort function
    nums3 = quicksort(nums1 + nums2)
    return median_calc(nums3)

print(findMedianSortedArrays(nums1, nums2))



