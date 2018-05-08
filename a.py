# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def search1(Ci, a): 
    # find index of first elem in Ci s.t. Ci[l1][0]>= a 
    l, r = 0, len(Ci) - 1 
    while l < r: 
        m = l + (r-l)//2 
        if Ci[m][0] < a: 
            l = m +1
        # elif Ci[m][0] > a: 
        #     r = m 
        else: 
            r = m 
    return l 
    
def search2(Ci, b): 
    # find index of last elem  in Ci s.t. Ci[l2][0] <= b 
    l, r = 0, len(Ci) - 1 
    while l < r: 
        m = r - (r-l)//2 
        if Ci[m][0] > b: 
            r = m -1
        else: 
            l = m 
    return r  
            
    
    
    
def solution(A, B, C):
    # write your code in Python 3.6
    # pass
    if len(A) == 0: return 0
    N = len(A) 
    M = len(C) 
    Ci = [(C[i], i) for i in range(M)]
    # Cim = [(-c[0], c[)] 
    Ci.sort(key = lambda x: x[0]) 
    res = -1 
    for k in range(N): 
        l1 = search1(Ci, A[k]) 
        if l1 == -1: return -1 
        l2 = search2(Ci, B[k]) 
        # print (l1, l2)
        if l2 == -1: return -1 
        tmp = float('inf') 
        for l in range(l1, l2+1): 
            tmp = min(tmp, Ci[l][1]) 
        res = max(res, tmp) 
    return res + 1 
    
A = [1, 4, 5, 8]
B = [4, 5, 9, 10]
C = [4, 6, 7, 10, 2]

print(solution(A, B, C))