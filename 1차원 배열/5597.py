arr = [False] * 30

for i in range(28):
    arr[int(input()) - 1] = True

index = 0
for i in arr:
    if i == False:
        print(index + 1)
    index = index + 1