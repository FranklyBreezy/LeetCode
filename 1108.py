class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.','[.]')

        """
        new = []
        for letter in address:
            if letter == '.':
                new.append("[.]")
            else:
                new.append(letter)
        return ''.join(new)
        """
#Time complexity: O(n) - where n is the length of the input string.
#The .replace() method scans the string once and builds the new string in one pass.

#Space complexity: O(n) - a new string is created as strings in python are immutable.
#It's proportional to the size of the input as each '.' becomes '[.]', (i.e 1 char -> 3 chars).