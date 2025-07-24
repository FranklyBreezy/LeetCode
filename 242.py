class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        """
        alph = []
        for letter in s:
            alph.append(letter)
        for letter in t:
            if letter in alph:
                alph.remove(letter)
            else:
                return False
        if len(alph) == 0:
            return True
        return False
        """

        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        """
        if len(s) != len(t):
            return False

        counts = [0]*26
        for letter in s:
            i = ord(letter)-ord('a')
            counts[i] += 1
        for letter in t:
            i = ord(letter)-ord('a')
            counts[i] -= 1
            if counts[i] < 0:
                return False
        return True