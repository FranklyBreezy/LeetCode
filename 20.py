class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {'(':')',"[":"]","{":"}"}
        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack or mapping[stack.pop()] != char:
                    return False
        return not stack
    
# Time complexity: O(n)
# We traverse the string once, and each character is pushed and popped from the stack at most once.
# Lookup in the dictionary and stack operations are all O(1), so total time is linear in the size of the input string.

# Space complexity: O(n)
# In the worst case (e.g., all opening brackets), the stack can grow to the size of the input string.
# The dictionary has a fixed size (constant space), so total space is linear in the input size.
