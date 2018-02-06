


def lcs(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    trace = [[0 for _ in range(n+1)] for _ in range(m+1)]
    # dp[i,j] is the lcs(X[:i], Y[:i])
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                trace[i][j] = 0
            else:
                if dp[i-1][j] < dp[i][j-1]: 
                    trace[i][j] = -1
                    dp[i][j] = dp[i][j-1]
                else: 
                    trace[i][j] = 1
                    dp[i][j] = dp[i-1][j]
    return dp[m][n], trace

def print_trace(trace, X, i, j):
    if i == 0 or j == 0: return 
    if trace[i][j] == 0: 
        print_trace(trace, X, i-1, j-1)
        print X[i-1],
    elif trace[i][j] == -1 :
        print_trace(trace, X, i, j-1)
        # print X[i]
    else: print_trace(trace, X, i-1, j)


X = 'bdc'
Y = 'bc'

l, trace = lcs(X, Y)
print_trace(trace, X, len(X), len(Y))