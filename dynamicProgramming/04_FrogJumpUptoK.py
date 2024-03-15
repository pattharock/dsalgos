import sys

def recursion(n, k, height):
    if n < 0:
        return float("inf")
    if n == 0:
        return 0
    minCost = float("inf")
    for i in range(1, k + 1):
        if (n - i >= 0):
            thisJumpCost = recursion(n-i, k, height) + abs(height[n] - height[n-i])
            minCost = min(minCost, thisJumpCost)
    return minCost

def memoization(n, k, height, memo):
    if n in memo:
        return memo[n]
    if n < 0:
        return float("inf")
    if n == 0:
        return 0
    minCost = float("inf")
    for i in range(1, k + 1):
        if (n - i >= 0):
            thisJumpCost = memoization(n-i, k, height, memo) + abs(height[n] - height[n-i])
            minCost = min(minCost, thisJumpCost)
    memo[n] = minCost
    return memo[n]

def tabulation(n, k, height):
    dp = [0 for i in range(n)]
    dp[0] = 0
    for i in range(1, n):
        minCost = sys.maxsize
        for k in range(1, k + 1):
            if i >= k:
                thisJumpCost = dp[i-k] + abs(height[i] - height[i - k])
                minCost = min(minCost, thisJumpCost)
        dp[i] = minCost
    return dp[len(dp)-1]

def frogJump(n, k, height):
    pass

def prettyPrint(n, k, height):
    print(f"[RECURSION] frogJump({n}, {k}): {recursion(n - 1, k, height)}")
    print(f"[MEMOIZATION] frogJump({n}, {k}): {memoization(n - 1, k, height, {})}")
    print(f"[TABULTAION] frogJump({n}, {k}): {tabulation(n, k, height)}")
    print()

def main():
    n = int(input("N: "))
    k = int(input("K: "))
    inputList = []
    for i in range(n):
        element = int(input(f"height[{i}]: "))
        inputList.append(element)
    prettyPrint(n, k, inputList)

if __name__ == "__main__":
    main()
