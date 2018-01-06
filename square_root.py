'''
Square root 
given an non negative integer a, return int(a**.5) without using **.5 
'''

''' IDEA 
binary search 
note: avoid overflow 
'''

class Solution(object):
    # O(n)
    def square_root(self, a):
        if a == 0: return 0 
        if a < 4: return 1 
        left, right = 2, a//2 
        while left <= right:
            mid = left + (right - left)//2
            other = a//mid #integer division 
            if other == mid:
                return mid 
            if other < mid: # need to reduce mid 
                right = mid - 1
            else: 
                left = mid + 1
        return mid 

        


tests = [ (0, 0),
          (1, 1), 
          (2, 1), 
          (8, 2), 
          (9, 3), 
          (100, 10), 
          (99, 9), 
          (101, 10), 
          (10, 3), 
          (1073741824, 32768)
          ]


for test in tests:
    out = Solution().square_root(test[0])
    assert out == test[-1], "incorrect in " + str(test) + ", out = " + str(out)

print "All tests passed!"
