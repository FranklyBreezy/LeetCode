class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1

        for j in range(i,len(nums)):
            nums[j] = 0
        
# Time complexity: O(n)
# We traverse the array twice:
#   - First pass moves all non-zero elements to the front.
#   - Second pass fills in the remaining positions with zeros.
# Each element is accessed at most once, so total operations are linear in the size of the array.

# Space complexity: O(1)
# The algorithm modifies the input array in-place and uses only a constant amount of extra space (one index variable).


        

        