class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for i in s:
            if i.isalpha() or i.isdigit():
                st.append(i.lower())
        s = ''.join(st)
        if s != s[::-1]:
            return False
        return True
        
# Time Complexity: O(n)
# - One pass to filter and normalize the characters.
# - One pass to compare the string with its reverse.

# Space Complexity: O(n)
# - You build a new string (or list of chars) with only alphanumeric characters.
