class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        add = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            add.append(total)
        return add 

# Time complexity: O(n) – where n is the number of elements in the input list 'nums'.
# Only one pass through the list is made, and each operation (addition and append) takes constant time.

# Space complexity: O(n) – due to the result list 'add' that stores the running sums for each element.
# No extra data structures (like nested loops or slicing) are used, so it's memory-efficient.
