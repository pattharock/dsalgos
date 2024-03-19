def recursion(n, nextDayActivityIndex, inputMatrix):
    if n == 0:
        maximumScore = 0
        for i in range(3):
            if i != nextDayActivityIndex:
                maximumScore = max(maximumScore, inputMatrix[0][i])
        return maximumScore
    else:
        maximumScore = 0
        for i in range(3):
            if i != nextDayActivityIndex:
                maximumScore = max(maximumScore, inputMatrix[n][i] + recursion(n-1, i, inputMatrix))
        return maximumScore

def memoization(n, nextDayActivityIndex, inputMatrix, memo):
    if (memo[n][nextDayActivityIndex] != -1):
        return memo[n][nextDayActivityIndex]
    if (n == 0):
        maximumScore = 0
        for i in range(3):
            if (i != nextDayActivityIndex):
                maximumScore = max(maximumScore, inputMatrix[0][i])
        memo[n][nextDayActivityIndex] = maximumScore
        return memo[n][nextDayActivityIndex]
    else:
        maximumScore = 0
        for i in range(3):
            if (i != nextDayActivityIndex):
                maximumScore = max(maximumScore, inputMatrix[n][i] + memoization(n-1, i, inputMatrix, memo))
        memo[n][nextDayActivityIndex] = maximumScore
        return memo[n][nextDayActivityIndex]

def tabulation(n, inputMatrix):
    dp = [[0 for i in range(4)] for j in range(len(inputMatrix))]
    dp[0][0] = max(inputMatrix[0][1], inputMatrix[0][2])
    dp[0][1] = max(inputMatrix[0][0], inputMatrix[0][2])
    dp[0][2] = max(inputMatrix[0][0], inputMatrix[0][1])
    dp[0][3] = max(inputMatrix[0][0], inputMatrix[0][1], inputMatrix[0][2])
    for day in range(n + 1):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    dp[day][last] = max(dp[day][last], inputMatrix[day][task] + dp[day - 1][task])
    return dp[len(dp)-1][3]

def prettyPrint(inputMatrix):
    memo = [[-1 for i in range(4)] for j in range(len(inputMatrix))]
    print(f"[RECURSION] ninjaTraining({len(inputMatrix)}): {recursion(len(inputMatrix) - 1, 3, inputMatrix)}")
    print(f"[MEMOIZATION] ninjaTraining({len(inputMatrix)}): {memoization(len(inputMatrix) - 1, 3, inputMatrix, memo)}")
    print(f"[TABULATION] ninjaTraining({len(inputMatrix)}): {tabulation(len(inputMatrix) - 1, inputMatrix)}")
    print()

def main():
    n = int(input("N: "))
    inputMatrix = [[-1 for i in range(3)] for j in range(n)]
    for i in range(n):
        for j in range(3):
            element = int(input(f"matrix[{i}][{j}]: "))
            inputMatrix[i][j] = element
    prettyPrint(inputMatrix)

if __name__ == "__main__":
    main()
