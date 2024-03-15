def recursion(n, height):
    if n <= 0:
        return 0
    if n == 1:
        singleJumpCost = recursion(n-1, height) + abs(height[n] - height[n-1])
        return singleJumpCost
    singleJumpCost = recursion(n-1, height) + abs(height[n] - height[n-1])
    doubleJumpCost = recursion(n-2, height) + abs(height[n] - height[n-2])
    return min(singleJumpCost, doubleJumpCost)

def memoization(n, height, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 0
        return 0
    if n == 1:
        memo[n] = memoization(n-1, height, memo) + abs(height[n] - height[n-1])
        return memo[n]
    singleJumpCost = memoization(n-1, height, memo) + abs(height[n] - height[n-1])
    doubleJumpCost = memoization(n-2, height, memo) + abs(height[n] - height[n-2])
    memo[n] = min(singleJumpCost, doubleJumpCost)
    return memo[n]

def tabulation(n, height):
    dp = [0 for i in range(n)]
    dp[0] = 0
    dp[1] = abs(height[1]-height[0])
    for i in range(2, len(dp)):
        dp[i] = min(
            dp[i-1] + abs(height[i] - height[i-1]),
            dp[i-2] + abs(height[i] - height[i-2])
        )
    return dp[len(dp) - 1]

def spaceOptimised(n, height):
    prev2 = 0
    prev = 0
    for i in range(1, len(height)):
        jumpOne = prev + abs(height[i] - height[i-1])
        if i != 1:
            jumpTwo = prev2 + abs(height[i] - height[i-2])
        else:
            jumpTwo = float("inf")
        curr = min(jumpOne, jumpTwo)
        prev2 = prev
        prev = curr
    return prev

def frogJump(n):
    pass

def prettyPrint(n, inputList):
    print(f"[RECURSION] climbingStairs({n}): {recursion(n - 1, inputList)}")
    print(f"[MEMOIZATION] climbingStairs({n}): {memoization(n - 1, inputList, {})}")
    print(f"[TABULATION] climbingStairs({n}): {tabulation(n, inputList)}")
    print(f"[SPACE OPTIMISED] climbingStairs({n}): {spaceOptimised(n, inputList)}")
    print()

def main():
    inputList = []
    n = int(input("N: "))
    for i in range(n):
        ele = int(input(f"inputList[{i}]: "))
        inputList.append(ele)
    prettyPrint(n, inputList)

if __name__ == "__main__":
    main()
