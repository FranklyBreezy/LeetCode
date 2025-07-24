import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output = []
        dq = collections.deque()
        l = r = 0

        while r < len(nums):
            # Remove all smaller elements from the back
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            # Remove elements out of the current window
            if l > dq[0]:
                dq.popleft()
            
            # Start appending to output when window is fully formed
            if (r + 1) >= k:
                output.append(nums[dq[0]])
                l += 1  # Slide the left of the window

            r += 1

        return output

# Time complexity: O(n)
# Each index is added to and removed from the deque at most once.
# All operations inside the loop (append, pop, popleft) are constant time.
# Therefore, the entire algorithm runs in linear time relative to the length of the input list.

# Space complexity: O(k)
# In the worst case, the deque can store up to k indices (when all elements are in decreasing order).
# Output list also takes O(n - k + 1) space to store the max of each window.
