N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(i + 1)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

for i in range(M):
    start, end = map(int, input().split())
    swap(arr, start - 1, end - 1)

for i in arr:
    print(i, end=" ")