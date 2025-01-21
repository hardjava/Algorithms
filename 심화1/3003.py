standard = [1, 1, 2, 2, 2, 8]
arr = list(int(i) for i in input().split())

for i in range(len(standard)):
    print(standard[i] - arr[i], end=' ')