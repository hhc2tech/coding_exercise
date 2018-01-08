
'''
https://leetcode.com/problems/rotate-image/description/
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''

''' IDEA 
2. swap four corner then ...
1. flip updown then transpose for clockwise, transpose then flip updown for 
counter clockwise 
'''
class Solution(object):
    def rotate(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m.reverse()
        for i in range(len(m)):
            for j in range(i+1, len(m)):
                m[i][j], m[j][i] = m[j][i], m[i][j]
        return m

    def rotate2(self, m):
        n = len(m)
        for i in range(n//2):
            for j in range(i, n-i-1):
                m[i][j], m[j][n-i-1], m[n-i-1][n-j-1], m[n-j-1][i] = \
                    m[n-j-1][i], m[i][j], m[j][n-i-1], m[n-i-1][n-j-1]
        return m 

m = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

m2 = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
print(Solution().rotate2(m2))