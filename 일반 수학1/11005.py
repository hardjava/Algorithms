arr = []
N, M = map(int, input().split())

while N > 0:
    arr.append(N % M)
    N //= M

for i in range(len(arr)):
    if arr[i] >= 10:
        arr[i] = chr((arr[i] - 10) + ord('A'))

arr.reverse()

print("".join(map(str, arr)))