'''
This problem is from
https://leetcode.com/problems/ugly-number-ii/description/
rite a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
'''

# idea: 
# compute first n ugly number 
# if the next number in the list caused by *2 -> store i2, *3 -> i3, *5 -> i5.
# at each step, compare ugly[i2]*2, ugly[i3]*3, ugly[i5]*5. If the minimum appears 
# at i2 -> increase i2 by 1. Similarly for i3 and i5. 

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]*(n+1) # pre allocating if often faster
        i2 = i3 = i5 = 0 
        for i in range(n):
            n2, n3, n5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
            new_num = min(n2, n3, n5)
            if new_num == n2: i2 += 1
            if new_num == n3: i3 += 1
            if new_num == n5: i5 += 1 
            ugly[i+1] = new_num
        return ugly[n-1]
        
tests = [ (1, 1),
          (5, 5),
          (10, 12)]

for test in tests:
    assert Solution().nthUglyNumber(test[0]) ==test[1], "incorrect in " + str(test)

print "All tests passed!"