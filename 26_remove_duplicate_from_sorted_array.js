/***
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order. **/

// -----------------------------------------------------------------

// set an inital counter to keep track of the checked number
// iterate through the array of numbers
// check to see if the current number is the same as checked number
// if yes:
    // set the current nubmer as the next number in the array
    // increment the counter
// if no:
    // go to the next number in the array


var removeDuplicates = function(nums) {
  let current_num = 0
  for(let i = 1; i< nums.length; i++){
      if(nums[current_num] != nums[i]){
          current_num++
          nums[current_num] = nums[i]
      }   
  }
  return (current_num + 1)
};

/* 

nums = [1,1,2]

current_num = 0
i = 1
check if nums[0] 1= nums[1] 
1 == 1
current_num = 1
nums[1] = nums[1]
-iterate-
check 1 != 2
current_num = 1
nums[1] == nums[2] 
nums = [1, 2, ]
return 2


*/