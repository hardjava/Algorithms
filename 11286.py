from queue import PriorityQueue
import sys
input = sys.stdin.readline

que = PriorityQueue()
N = int(input())
result = []
for i in range(N):
    enter = int(input())
    value = (abs(enter), enter)
    if enter != 0:
        que.put(value, enter)
    else:
        if que.empty():
            print(0)
        else:
            print(que.get()[1])