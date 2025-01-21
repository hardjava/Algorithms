
def fill(arr, x, y):
    for i in range(1,11):
        for j in range(1,11):
            arr[i + x][j + y] = 1

N = int(input())

arr = []
for i in range(101):
    arr.append(list(0 for j in range(101)))

for i in range(N):
    x, y = map(int, input().split())
    fill(arr, x, y)

count = 0

for i in range(1, 101):
    for j in range(1, 101):
        count += arr[i][j]

print(count)