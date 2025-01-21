import sys
from collections import deque
input = sys.stdin.readline
N, L = map(int, input().split())
myList = list(map(int, input().split()))
myDeque = deque()

for i in range(N):
    while len(myDeque) != 0 and myDeque[-1][0] > myList[i]:
        myDeque.pop()
    myDeque.append((myList[i], i))
    if myDeque[0][1] <= i - L:
        myDeque.popleft()
    print(myDeque[0][0], end= ' ')