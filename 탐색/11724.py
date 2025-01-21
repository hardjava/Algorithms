from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False] * (N + 1)
count = 0

def visit(current):
    s = [current]
    while len(s) != 0:
        c = s.pop()
        if visited[c] == False:
            visited[c] = True
            for j in arr[c]:
                s.append(j)
                
for i in range(1, N + 1):
    if visited[i] == False:
        count += 1
        visit(i)
        
print(count)