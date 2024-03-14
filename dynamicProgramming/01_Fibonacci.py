def recursion(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursion(n - 1) + recursion(n - 2)

def memoization(n, memo):
    if n in memo:
        return memo[n]
    if n < 0:
        return -1
    if n == 0:
        memo[n] = 0
        return memo[n]
    if n == 1:
        memo[n] = 1
        return memo[n]
    memo[n] = memoization(n - 1, memo) + memoization(n - 2, memo)
    return memo[n]

def tabulation(n):
    dp = [0 for i in range(n + 1)]
    dp[0], dp[1] = 0, 1
    for i in range(2, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

def fibonacci(n):
    return recursion(n)

def main():
    n = int(input("N: "))
    print(f"[RECURSION] fib({n}): {recursion(n)}")
    print(f"[MEMOIZATION] fib({n}): {memoization(n, {})}")
    print(f"[TABULATION] fib({n}): {tabulation(n)}")
    print()

if __name__ == "__main__":
    main()
