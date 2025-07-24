# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize dummy and current pointer
        dummy = ListNode(0)
        current = dummy
        
        # Pointers to traverse both lists
        one = list1
        two = list2
        
        # Traverse both lists
        while one and two:
            if one.val < two.val:
                current.next = one
                one = one.next
            else:
                current.next = two
                two = two.next
            current = current.next
        
        # Attach leftover nodes if any
        if one:
            current.next = one
        if two:
            current.next = two
        
        # Return the merged list head
        return dummy.next
    
# Time complexity: O(n + m)
# We traverse each node in both lists exactly once,
# where n and m are the lengths of list1 and list2 respectively.

# Space complexity: O(1)
# We rearrange the existing nodes’ pointers in-place,
# using only a few extra pointers regardless of input size.
