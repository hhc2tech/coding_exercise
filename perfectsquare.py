'''
This problem is from
https://leetcode.com/problems/perfect-squares/description/
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

'''
from time import time 


import collections

class Solution(object):
    # DP solution
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp 
        while len(dp) <= n:
            dp += [min(dp[-i*i] for i in range(1, int(len(dp)**0.5)+1)) + 1]
        return dp[n]
    
    # BFS solution 
    # def numSquares(self, n):
    #     if n < 2: return n 
    #     sqs = [i*i for i in range(1, int(n**.5)+1)]
    #     if sqs[-1] == n: return 1 
    #     # remain = set([n])
    #     remain = {n}
    #     cnt = 0 
    #     while remain: 
    #         cnt += 1
    #         tmp = set()
    #         for m in remain:
    #             for s in sqs:
    #                 if s > m: break 
    #                 if s == m: return cnt 
    #                 tmp.add(m-s)
    #         remain = tmp 

    # def numSquares(self,n):
    #     dp = [0]*(n+1)
    #     for i in range(1, n+1):
    #         dp[i] = min([dp[i-j*j] for j in range(1, int(i**.5)+1)]) + 1
    #     return dp[-1]




tests = [ (0, 0), 
          (1, 1),
          (2, 2),
          (3, 3),
          (4, 1),
          (12, 3),
          (13, 2)
          ]


# for test in tests:
#     out = Solution().numSquares(test[0])
#     assert out == test[1], "incorrect in " + str(test) + ", out = " + str(out)

# print "All tests passed!"
t1 = time()
print Solution().numSquares(7168)
print time() - t1
print "Done"