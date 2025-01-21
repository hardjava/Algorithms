arr = [3] * 26

for i in range(1, 18):
    if i % 3 != 0:
        arr[i] = arr[i - 1]
    else:
        arr[i] = arr[i - 1] + 1

arr[18] = arr[17]
a = 0
for i in range(19, 25):
    if a % 3 == 0:
        arr[i] = arr[i - 1] + 1
    else:
        arr[i] = arr[i - 1]
    a += 1

arr[25] = arr[24]


sum = 0
str = input()

for i in str:
    sum += arr[ord(i) - ord('A')]

print(sum)