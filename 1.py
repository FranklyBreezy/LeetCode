class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        i = 0
        j = i+1
        sum = nums[i]+nums[j]
        if sum == target:
            return (i,j)
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    return (i,j)
        return (-1,-1)
        """

        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed],i]
            else:
                seen[nums[i]] = i
        return (-1,-1)

# Time complexity: O(n) — where n is the number of elements in the input list `nums`.
# Each element is visited exactly once in a single loop, and dictionary operations (insertion & lookup) are O(1) on average.

# Space complexity: O(n) — due to the hash map (dictionary) `seen` which stores up to n key-value pairs (each number and its index).
# Hash map is used for efficient constant-time lookups to find complements of the current number (target - num).
