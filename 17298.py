import sys
input = sys.stdin.readline

N = int(input())
enterList = list(map(int, input().split()))
result = [0] * N
s = []
idx = N - 1
while idx >= 0:
    if len(s) == 0:
        result[idx] = -1
    else:
        while len(s) and s[-1] <= enterList[idx]:
            s.pop()
        if len(s) == 0:
            result[idx] = -1
        else:
            result[idx] = s[-1]
    s.append(enterList[idx])
    idx -= 1

print(' '.join(map(str, result)))