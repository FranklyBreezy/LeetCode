class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start <= end:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            start += 1
            end -= 1
        return -1

# Time complexity: O(n)
# In the worst case, we scan from both ends toward the middle.
# Each element is checked at most once, so total comparisons are linear in the size of the array.

# Space complexity: O(1)
# We only use two pointers (start and end), so extra space usage is constant.
