import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [[0] * (N + 1) for _ in range(N + 1)]
A = [[0] * (N + 1)]

for _ in range(1, N + 1):
    temp = [0]
    inputList = list(map(int, input().split()))
    temp.extend(inputList)
    A.append(temp)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + A[i][j]    

for _ in range(M):
    startRow, startCol, endRow, endCol = map(int, input().split())
    print(S[endRow][endCol] - S[endRow][startCol - 1] - S[startRow - 1][endCol] + S[startRow - 1][startCol - 1])