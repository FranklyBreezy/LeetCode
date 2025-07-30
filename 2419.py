class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mVal = max(nums)
        curr_len = 0
        max_len = 0
        for num in nums:
            if num == mVal:
                curr_len += 1
                max_len= max(max_len,curr_len)
            else:
                curr_len = 0
        return max_len
        
#Time Complexity: O(n) 
# - We use the built-in max() function which takes O(n) time to find the maximum element.
# - We then iterate through the array once more in a single pass (O(n)) to count the longest contiguous subarray of max elements.
# - Thus, total time complexity is O(n) + O(n) = O(n).

# Space Complexity: O(1)
# - We use a constant amount of extra space: a few integer variables (mVal, curr_len, max_len).
# - No additional space is used proportional to the input size.