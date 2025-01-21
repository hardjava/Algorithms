import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sumArr = [0]
for i in range(1, len(arr) + 1):
    sumArr.append(sumArr[i - 1] + arr[i - 1])

for i in range(M):
    start, end = map(int, input().split())
    value = sumArr[end] - sumArr[start - 1]
    print(value)