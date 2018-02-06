'''
https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
'''

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        55ms, 16% 
        """
        if len(nums) < 2: return len(nums)
        cur_len = 1
        best_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: 
                cur_len += 1
            else:
                best_len = max(best_len, cur_len)
                cur_len = 1
        best_len = max(best_len, cur_len)
        return best_len 
                



tests = [ ([], 0), 
          ([1], 1),
          ([1, 2], 2),
          ([1, 2, 2, 3], 2),
          ([4, 3, 2, 1], 1),
          ([2, 2], 1),
          ([1, 2, 3, 5], 4)
          ]


for test in tests:
    out = Solution().findLengthOfLCIS(test[0])
    assert out == test[1], "incorrect in " + str(test) + ", out = " + str(out)

print "All tests passed!"

# class ClassName(object):
#     """docstring for ClassName"""
#     def __init__(self, arg):
#         super(ClassName, self).__init__()
#         self.arg = arg
        