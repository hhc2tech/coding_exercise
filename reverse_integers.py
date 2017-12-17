'''
This problem is from
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.
Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
# idea 1
# separate sign (s) and abs value (v)
# using ``a`` to convert an integer `a` to a string 
# using `str0[::-1]` to reverse a string 
# if value >= 2**31, then return 0 
#########
# idea 2 
# get each digit from the end

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = cmp(x, 0)
        r = int(`s*x`[::-1])
        return s*r*(r < 2**31)

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        # pass 
        s = cmp(x, 0)
        y = x*s 
        res = 0 
        while y > 0:
            last_digit = y%10 
            res = res*10 + last_digit
            if res >= 2**31: return 0 
            y /= 10 
        return res*s 


tests = [ (123, 321),
          (-123, -321),
          (2**31, 0),
          (0, 0),
          (22, 22),
          (120, 21),
          (1000, 1)]

for test in tests:
    assert Solution().reverse2(test[0]) ==test[1], "incorrect in " + str(test)

print "All tests passed!"