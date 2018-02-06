'''
https://leetcode.com/problems/maximum-product-of-three-numbers/description/
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
 [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24

Example 3:
Input: [-3, -2, -1, 0, 1]
Output: 6

Ex4:
Input: [-4, -3, -2, -1]
Output: -6

IDEA: 
sort the array first. The maximum will be either nums[-1]*nums[-2]*nums[-3] or 
nums[-1]*nums[1]*nums[0]
'''


from time import time 
import heapq 
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])

    # faster 
    # find 3 largest and 2 smallest only 
    def maximumProduct2(self,nums):
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0]*a[1]*a[2], a[0]*b[1]*b[0])

tests = [ ([1,2,3], 6),
        ([1,2,3,4], 24),
        ([-3, -2, -1, 0, 1], 6),
        ([-4, -3, -2, -1], -6)]


for test in tests:
    out = Solution().maximumProduct2(test[0])
    assert out == test[1], "incorrect in " + str(test) + ", out = " + str(out)

print "All tests passed!"
# t1 = time()
# print Solution().numSquares(7168)
# print time() - t1
# print "Done"