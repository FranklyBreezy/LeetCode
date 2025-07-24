class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(2*len(nums)):
            """
            if i < len(nums):
                ans.append(nums[i])
            else:
                ans.append(nums[i-len(nums)])
            """
            ans.append(nums[i%len(nums)])
        return ans

#Time complexity: O(n) - where n is 2 * len(nums). Each index is visited exactly once.
#Space complexity: O(n) - a new list of size 2 * n is created to store the result.
#The use of i % len(nums) allows us to loop over the original array twice without conditionals.