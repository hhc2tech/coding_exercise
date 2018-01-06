'''
This problem is from
https://leetcode.com/problems/01-matrix/description/
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0

Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.

'''

# idea: using a queue
# find all 0 (depth = 0), push them into queue
# pop a 0, find all neighbors of 0 which are not seen, depth = 1, push them into queue 
# continue this process until the queue is empty 
# leetcode 997 ms (47%)


import collections

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        res = [[0]*n for _ in range(m)]
        q = collections.deque([(i, j, 0) for i in range(m) for j in range(n) if matrix[i][j] == 0])
        # seen = {(x, y) for x, y, _ in q}
        visited = [[False]*n for _ in range(m)]
        for x,y,_ in q: 
            visited[x][y] = True 
        while q: 
            i, j, depth = q.popleft()
            res[i][j] = depth
            for d in dirs:
                x, y = i + d[0], j + d[1]
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    visited[x][y] = True 
                    q.append((x, y, depth + 1))
        return res 


tests = [ ([[0]], [[0]]),
          ([[0, 0]], [[0, 0]]),
          ([[0, 1]], [[0, 1]]),
          ([[0,1], [1, 1]], [[0, 1], [1, 2]]),
          ([[0,0,0],[0,1,0],[0,0,0]], [[0,0,0],[0,1,0],[0,0,0]]), 
          ([[0, 1, 0], [0, 1, 0]], [[0, 1, 0], [0, 1, 0]]),
          ([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]], [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]), 
          ]

for test in tests:
    out = Solution().updateMatrix(test[0])
    assert out == test[1], "incorrect in " + str(test) + ", out = " + str(out)

print "All tests passed!"