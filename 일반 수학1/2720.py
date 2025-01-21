def getCout(num, cent):
    count = 0
    while num - cent >= 0:
        count += 1
        num -= cent
    return num,count

N = int(input())
arr = [25, 10, 5, 1]
result = list(0 for i in range(4))
for i in range(N):
    num = int(input())
    for j in range(4):
        num, result[j] = getCout(num, arr[j])
    print(" ".join(map(str, result)))