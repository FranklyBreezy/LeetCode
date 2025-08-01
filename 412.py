class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                arr.append("FizzBuzz")
            elif i % 3 == 0 and not i % 5 == 0:
                arr.append("Fizz")
            elif i % 5 == 0 and not i % 3 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(i)) 
        return arr
    
#Time complexity: O(n) - where n is the input number.
#The function interates from 1 to n exactly once and performs constant-time checks and appends for each iteration.

#Space complexity: O(n) - the output list 'arr' stores a string for each number from 1 to 'n'.

