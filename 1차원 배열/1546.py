N = int(input())
arr = []

for i in input().split():
    arr.append(int(i))

maximum = max(arr)

for index in range(len(arr)):
    arr[index] = arr[index] / maximum * 100

print(sum(arr) / len(arr))