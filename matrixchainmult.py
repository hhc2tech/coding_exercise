
# def matrix_chain_order(p):
#     '''
#     m[i][j]: min cost of computer Ai...Aj, i = 0, break point is k = s[i][j]
#     (Ai..k)(Ak+1..j) cost p[i]p[k+1]p[j+1]
#     A[i] has size p[i] x p[i+1]
#     '''
#     N = len(p)-1 # number of matrixes 
#     m = [[0 for _ in range(N)] for _ in range(N)]
#     s = [[0 for _ in range(N)] for _ in range(N)]
#     # l is chain length 
#     for l in range(2, N+1):
#         for i in range(N-l+1):
#             j = i + l -1 
#             m[i][j] = float('inf')
#             for k in range(i, j):
#                 # import pdb; pdb.set_trace()  # breakpoint 8559668b //
#                 q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
#                 if q < m[i][j]:
#                     m[i][j] = q 
#                     s[i][j] = k 
#     return m, s 


p = [30, 35, 15, 5, 5, 10, 20, 25] # three matrices 
# m, s = matrix_chain_order(p)
# # print len(s)
# # print m 
# def print_sol(s, i, j):
#     # if j - i < 2: 
#         # return
#     if i == j:
#         print "A%d"%i,
#     else:
#         print '(',
#         k = s[i][j]
#         # print i,j, k
#         print_sol(s, i, k),
#         print_sol(s, k+1, j)
#         print ')',

# print_sol(s, 0, len(p)-2)

#### second time 
def matrix_chain(p):
    '''
    Ai has size p[i] x p[i+1]
    Ai...Aj has cost m[i][j] with separate at k = s[i][j]
    Ai...Aj = (Ai...k)(Ak+1..j)
    => m[i][j] = min(m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1])
    '''
    N = len(p) - 1 # number of matrices 
    m = [[0 for _ in range(N)] for _ in range(N)]
    s = [[0 for _ in range(N)] for _ in range(N)]
    # let l is length of chain 
    for l in range(2, N+1):
        for i in range(N-l+1):
            j = i + l - 1 
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j] = q 
                    s[i][j] = k 
    return m, s 

import sys 
def print_sol(s, i, j):
    if i == j:
        # print 'A%d'%i,
        sys.stdout.write('A' + str(i))  
    else:
        # print '(',
        sys.stdout.write('(')
        k = s[i][j]
        print_sol(s, i, k)
        print_sol(s, k+1, j)
        sys.stdout.write(')')
        # print ')',

p = [30, 35, 15, 5, 5, 10, 20, 25]
m, s = matrix_chain(p)
# print m, s

print_sol(s, 0, len(p) - 2)
# sys.stdout.write('a')
# sys.stdout.write('a')