def recursion(m, n):
    if m < 0 or n < 0:
        return 0
    if m == 0 or n == 0:
        return 1
    return recursion(m - 1, n) + recursion(m, n - 1)

def memoization(m, n, memo):
    if memo[m][n] != -1:
        return memo[m][n]
    if m < 0 or n < 0:
        return 0
    if m == 0 and n == 0:
        memo[m][n] = 1
        return memo[m][n]
    memo[m][n] = memoization(m - 1, n, memo) + memoization(m, n - 1, memo)
    return memo[m][n]

def tabulation(m, n):
    dp = [[0 for i in range(n)] for j in range(m)]
    dp[0][0] = 1

    for i in range(len(dp[0])):
        dp[0][i] = 1

    for j in range(len(dp)):
        dp[j][0] = 1

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]

def prettyPrint(m, n):
    memo = [[-1 for i in range(n)] for j in range(m)]
    print(f"[RECURSION] gridUniquPaths({m}, {n}): {recursion(m - 1, n - 1)}")
    print(f"[MEMOIZATION] gridUniquPaths({m}, {n}): {memoization(m - 1, n - 1, memo)}")
    print(f"[TABULATION] gridUniquPaths({m}, {n}): {tabulation(m, n)}")
    print()

def main():
    m = int(input("M: "))
    n = int(input("N: "))
    prettyPrint(m, n)

if __name__ == "__main__":
    main()
