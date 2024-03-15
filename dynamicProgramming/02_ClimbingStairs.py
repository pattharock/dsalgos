def recursion(n):
    if (n < 0):
        return 0
    if (n == 0):
        return 1
    return recursion(n-1) + recursion(n-2)

def memoization(n, memo):
    if n in memo:
        return memo[n]
    if (n < 0):
        memo[n] = 0
        return 0
    if (n == 0):
        memo[n] = 1
        return 1
    memo[n] = memoization(n-1, memo) + memoization(n-2, memo)
    return memo[n]

def tabulation(n):
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[len(dp)-1]

def spaceOptimised(n):
    prev = 1
    prev2 = 1
    if n == 0:
        return 1
    if n == 1:
        return 1
    for i in range(n-1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev

def climbingStairs(n):
    pass

def prettyPrint(n):
    print(f"[RECURSION] climbingStairs({n}): {recursion(n)}")
    print(f"[MEMOIZATION] climbingStairs({n}): {memoization(n, {})}")
    print(f"[TABULATION] climbingStairs({n}): {tabulation(n)}")
    print(f"[SPACE OPTIMISED] climbingStairs({n}): {spaceOptimised(n)}")
    print()

def main():
   n = int(input("N: "))
   prettyPrint(n)

if __name__ == "__main__":
    main()
