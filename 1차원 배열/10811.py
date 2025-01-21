N, M = map(int, input().split())

def reverse(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start + 1
        end = end - 1

arr = [i + 1 for i in range(N)]

for i in range(M):
    start, end = map(int, input().split())
    reverse(arr, start -1, end - 1)

print(" ".join(map(str, arr)))