import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
inputList = [0]
inputList.extend(list(map(int, input().split())))
sumList = [0] * (N + 1)
remainList = [0] * M
result = 0

for i in range(1, len(inputList)):
    sumList[i] = sumList[i - 1] + inputList[i]

for i in range(1 , len(sumList)):
    remain = sumList[i] % M
    if remain == 0:
        result += 1
    remainList[remain] += 1

for i in remainList:
    if i >= 2:
        result += math.comb(i, 2)

print(result)