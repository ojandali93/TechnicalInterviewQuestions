# Given an integer x, return true if x is palindrome integer.

# Input: x = 121
# output: true

#--------------------

# reverse the integer and see if the reverse is identical to the original string

class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]