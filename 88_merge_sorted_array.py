# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and 
# nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

#------------------

# Create a copy of the first list to work with
# set the first point
# set the second pointer
# add n and m and set it as the index
# check of the second pointer is greater than or equal to n //
#                         first pointer is smaller than m and that current index is less 
#                         than the same value in the second list
#   if so, add the copy value to the result list
#   iterate the first pointer
#   else iterate the second pointer

#--------------------------

class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1_copy = nums1[:m] 
    p1 = 0
    p2 = 0
    
    for p in range(n + m):
      if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
        nums1[p] = nums1_copy[p1] 
        p1 += 1
      else:
        nums1[p] = nums2[p2]
        p2 += 1