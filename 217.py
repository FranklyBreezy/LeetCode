class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        if len(nums_set) != len(nums):
            return True
        else:
            return False
#Time complexity: O(n) - where n is the number of elements in the input list.
#Space complexity: O(n) - due to the addition set used to track unique elements.
#Set is used as it automatically eliminates duplicate values.