class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        arr = []
        length = 0
        for letter in s:
            if letter in arr:
                length = max(length, len(arr))
                idx = arr.index(letter)
                arr = arr[idx+1:]
                arr.append(letter)
            if letter not in arr:
                arr.append(letter)
        length = max(length, len(arr))
        return length    
        """
        l = 0
        ls = {}
        ml = 0

        for right in range(len(s)):
            char = s[right]

            if char in ls and ls[char] >= l:
                l = ls[char]+1
            
            ls[char] = right
            ml = max(ml, right-l+1)
        return ml

# Time complexity: O(n)
        # We iterate through the string once with the right pointer.
        # The left pointer only moves forward, never backward.
        # Each character is processed at most twice, resulting in linear time.

        # Space complexity: O(min(m, n))
        # We use a dictionary to store characters and their indices.
        # At most, the dictionary holds all unique characters in the current window,
        # which can be at most the size of the string or the character set.