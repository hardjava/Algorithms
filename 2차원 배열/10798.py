arr = []
maxJ = 0
for i in range(5):
    str = input()
    arr.append(list(i for i in str))
    maxJ = max(maxJ, len(arr[i]))

for i in range(maxJ):
    for j in range(5):
        try:
            print(arr[j][i], end='')
        except IndexError:
            print(end='')