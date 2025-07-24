class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        write_index = 1  
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index
# Time complexity: O(n)
# We iterate through the array once with a single pass, comparing adjacent elements.
# Each element is processed exactly once, so the runtime grows linearly with the input size.

# Space complexity: O(1)
# The algorithm modifies the input array in-place, using only a fixed number of variables.
# No extra data structures proportional to input size are used.
