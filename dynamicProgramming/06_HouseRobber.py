def recursion(n, inputList):
    if n < 0:
        return 0
    if n == 0:
        return inputList[0]
    return max(recursion(n-1, inputList), recursion(n-2, inputList) + inputList[n])

def memoization(n, inputList, memo):
    if n in memo:
        return memo[n]
    if n < 0:
        return 0
    if n == 0:
        memo[n] = inputList[0]
        return memo[n]
    memo[n] = max(memoization(n-1, inputList, memo), memoization(n-2, inputList, memo) + inputList[n])
    return memo[n]

def tabulation(n, inputList):
    dp = [0 for i in range(n)]
    dp[0] = inputList[0]
    for i in range(1, len(dp)):
        dp[i] = max(dp[i-1], dp[i-2] + inputList[i])
    return dp[len(dp) - 1]

def spaceOptimisation(n, inputList):
    prev2 = 0
    prev = inputList[0]
    for i in range(1, len(inputList)):
        curr = max(prev2 + inputList[i], prev2)
        prev2 = prev
        prev = curr
    return prev

def houseRobberRecursion(n, inputList):
    return max(recursion(n-2, inputList[1:]), recursion(n-2, inputList[:len(inputList)-1]))

def houseRobberMemoization(n, inputList):
    return max(memoization(n-2, inputList[1:], {}), memoization(n-2, inputList[:len(inputList)-1], {}))

def houseRobberTabulation(n, inputList):
    return max(tabulation(n-1, inputList[1:]), tabulation(n-1, inputList[:len(inputList)-1]))

def houseRobberSpaceOptimisation(n, inputList):
    return max(spaceOptimisation(n-1, inputList[1:]), spaceOptimisation(n-1, inputList[:len(inputList)-1]))

def prettyPrint(n, inputList):
    print(f"[RECURSION] maxNonAdjacentElementsSum({n}): {houseRobberRecursion(n, inputList)}")
    print(f"[MEMOIZATION] maxNonAdjacentElementsSum({n}): {houseRobberMemoization(n, inputList)}")
    print(f"[TABULATION] maxNonAdjacentElementsSum({n}): {houseRobberTabulation(n, inputList)}")
    print(f"[SPACE OPTIMISATION] maxNonAdjacentElementsSum({n}): {houseRobberTabulation(n, inputList)}")
    print()

def main():
    inputList = []
    n = int(input("N: "))
    for i in range(n):
        element = int(input(f"inputList[{i}]: "))
        inputList.append(element)
    prettyPrint(n, inputList)

if __name__ == "__main__":
    main()
