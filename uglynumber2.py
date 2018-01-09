'''
https://leetcode.com/problems/super-ugly-number/description/
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k <= 100, 0 < n <= 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.


'''
from time import time 
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        ns = [0]*len(primes)
        res = [1]*n
        for i in range(1,n):
            tmp = [res[ns[j]]*primes[j] for j in range(k)]
            res[i] = min(tmp)
            # res[i] = m 
            for j in range(k):
                if res[i] == tmp[j]: ns[j] += 1
        return res[-1]

    def nthUgleNumber(self, n):
        '''
        primes = [2, 3, 5]
        '''
        res = [1]*n 
        i2=i3=i5 = 0 
        for i in range(1,n):
            tmp2 = res[i2]*2
            tmp3 = res[i3]*3
            tmp5 = res[i5]*5
            m = min([tmp2, tmp3, tmp5])
            res[i] = m
            if m == tmp2: i2 += 1
            if m == tmp3: i3 += 1
            if m == tmp5: i5 += 1
        return res 

    def isUgly(self, num):
        """
        check if a number is a ugly number with factors 2, 3, 5
        :type num: int
        :rtype: bool
        """
        if num < 1: return False 
        while num > 1: 
            if num%5 == 0: 
                num/= 5
                continue 
            if num%3 == 0:
                num/= 3 
                continue 
            if num%2 == 0:
                num/=2 
                continue 
            return False
        return True 

    def isUgly2(self, num):
        if num < 1: return False 
        for p in [2, 3, 5]:
            while num%p == 0:
                num /= p 
        return num == 1

            

n = 12 
primes = [2, 7, 13, 19]            
print(Solution().nthSuperUglyNumber(n, primes))
print(Solution().nthUgleNumber(20))

print(Solution().isUgly2(1001))
# tests = [ (0, 0), 
#           (1, 1),
#           (2, 2),
#           (3, 3),
#           (4, 1),
#           (12, 3),
#           (13, 2)
#           ]


# # for test in tests:
# #     out = Solution().numSquares(test[0])
# #     assert out == test[1], "incorrect in " + str(test) + ", out = " + str(out)

# # print "All tests passed!"
# t1 = time()
# print Solution().numSquares(7168)
# print time() - t1
# print "Done"