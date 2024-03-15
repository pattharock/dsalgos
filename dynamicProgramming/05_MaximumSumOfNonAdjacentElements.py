from os import spawnve


def recursion(n, inputList):
    if n < 0:
        return 0
    if n == 0:
        return inputList[0]
    choiceOne = recursion(n-1, inputList)
    choiceTwo = inputList[n] + recursion(n-2, inputList)
    return max(choiceOne, choiceTwo)


def memoization(n, inputList, memo):
    if n in memo:
        return memo[n]
    if n < 0:
        return 0
    if n == 0:
        memo[n] = inputList[0]
        return memo[n]
    choiceOne = memoization(n-1, inputList, memo)
    choiceTwo = inputList[n] + memoization(n-2, inputList, memo)
    memo[n] = max(choiceOne, choiceTwo)
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
    curr = 0
    for i in range(1, len(inputList)):
        curr = max(prev2 + inputList[i], prev)
        prev2 = prev
        prev = curr
    return prev

def prettyPrint(n, inputList):
    print(f"[RECURSION] maxNonAdjacentElementsSum({n}): {recursion(n-1, inputList)}")
    print(f"[MEMOIZATION] maxNonAdjacentElementsSum({n}): {memoization(n-1, inputList, {})}")
    print(f"[TABULTAION] maxNonAdjacentElementsSum({n}): {tabulation(n, inputList)}")
    print(f"[SPACE OPTIMISATION] maxNonAdjacentElementsSum({n}): {spaceOptimisation(n, inputList)}")
    print()

def main():
    n = int(input("N: "))
    inputList = []
    for i in range(n):
        element = int(input(f"inputList[{i}]: "))
        inputList.append(element)
    prettyPrint(n, inputList)

if __name__ == "__main__":
    main()
