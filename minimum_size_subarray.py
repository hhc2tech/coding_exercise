'''
Binary search 
suppose that the list is already sorted 
'''


class Solution(object):
    # O(n)
    def binary_search(self, a, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right: 
            mid = (left + right) // 2
            b = nums[mid]
            if b == a: return mid
            if b < a: 
                left = mid + 1
            else: 
                right = mid-1 
        return -1 


        


tests = [ ([1, 2, 5, 6, 8, 100], -1, -1), 
        ([1, 2, 5, 6, 8, 100], 1, 0),
        ([1, 2, 5, 6, 8, 100], 100, 5),
        ([1, 2, 5, 6, 8, 100], 90, -1),
        ([1, 2, 5, 6, 8, 100], 2, 1),
        ([1, 2, 5, 6, 8, 100], 200, -1),
          ]


for test in tests:
    out = Solution().binary_search(test[1], test[0])
    assert out == test[-1], "incorrect in " + str(test) + ", out = " + str(out)

print "All tests passed!"
