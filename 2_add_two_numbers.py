# 2. Add two numbers: https://leetcode.com/problems/add-two-numbers/

# Summary: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#-------------------------------------------------

# Input: a list of linked list with values
# Output: the sum the two linked list

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]

# The pseudocode is as following:

# Initialize current node to dummy head of the returning list.
# Initialize carry to 00.
# Initialize pp and qq to head of l1l1 and l2l2 respectively.
# Loop through lists l1l1 and l2l2 until you reach both ends.
# Set xx to node pp's value. If pp has reached the end of l1l1, set to 00.
# Set yy to node qq's value. If qq has reached the end of l2l2, set to 00.
# Set sum = x + y + carrysum=x+y+carry.
# Update carry = sum / 10carry=sum/10.
# Create a new node with the digit value of (sum \bmod 10)(summod10) and set it to current node's next, then advance current node to next.
# Advance both pp and qq.
# Check if carry = 1carry=1, if so append a new node with digit 11 to the returning list.
# Return dummy head's next node.

class Solution:
  def addTwoNumbers(self, l1, l2 ,c = 0):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    val = l1.val + l2.val + c
    c = val // 10
    ret = ListNode(val % 10 ) 
    
    if (l1.next != None or l2.next != None or c != 0):
      if l1.next == None:
        l1.next = ListNode(0)
      if l2.next == None:
        l2.next = ListNode(0)
      ret.next = self.addTwoNumbers(l1.next,l2.next,c)
    return ret

